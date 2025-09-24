from __future__ import annotations

import logging
import secrets
import struct
import types
import typing

import siotls
from siotls import RaggedEOF, TLSError, key_logger
from siotls.crypto import TLSCipherSuite
from siotls.iana import AlertLevel, ContentType, TLSVersion
from siotls.language import TLSIO, TLSBufferError
from siotls.wrapper import WrappedSocket

from . import states
from .contents import ApplicationData, Content, Handshake, alerts
from .transcript import Transcript
from .utils import try_cast

if typing.TYPE_CHECKING:
    import socket
    from collections.abc import Iterable

    import siotls.configuration


logger = logging.getLogger(__name__)
cipher_plaintext = types.SimpleNamespace(
    must_encrypt=False,
    must_decrypt=False,
    should_rekey=False,
    tag_length=-1,  # trick so that +1 makes 0, see max_record_length
)
RECORD_HEADER_STRUCT = '!BHH'
RECORD_HEADER_LENGTH = struct.calcsize(RECORD_HEADER_STRUCT)

def startswith_change_cipher_spec(data):
    return data[0:1] == b'\x14' and data[3:6] == b'\x00\x01\x01'


class TLSConnection:
    config: siotls.configuration.TLSConfiguration
    """
    The TLS configuration used for establishing this secure connection.
    It includes this side (client / server) of the connection, but also
    the allowed ciphers, key exchanges and signature schemes and (many)
    other settings for this connection.
    """

    nconfig: siotls.configuration.TLSNegotiatedConfiguration | None
    """
    The cipher, key exchange, signature scheme and (many) other settings
    agreed upon by both peers during the handshake.
    """

    server_hostname: str | None
    """
    Client-side only. The expected server hostname, used for :ref:`SNI`
    and for verifying the CN and SAN fields for the server certificate.
    """

    def __init__(
        self,
        config: siotls.configuration.TLSConfiguration,
        server_hostname: str | None = None
    ):
        self.config = config
        self.nconfig = None
        self._cipher = cipher_plaintext
        self._signature = None

        self._transcript = Transcript({
            TLSCipherSuite[cipher_suite].digestmod
            for cipher_suite in config.cipher_suites
        })

        self._input_data = bytearray()
        self._input_handshake = bytearray()
        self._output_data = bytearray()
        self._application_data = bytearray()

        self._client_unique: bytes | None
        self._server_unique: bytes | None

        self._state: states.State

        if config.side == 'client':
            if not server_hostname:
                if config.trusted_public_keys:
                    w =("missing server_hostname, will reject all "
                        "certificates that do not hold one of the "
                        "trusted public keys")
                    logger.warning(w)
                elif config.truststore:
                    e =("server_hostname is mandatory with x509 "
                        "certificates, unless you provide a list of "
                        "trusted public keys.")
                    raise ValueError(e)
            self.server_hostname = server_hostname or None
            self._client_unique = secrets.token_bytes(32)
            self._server_unique = None
            self._state = states.ClientStart(self)
        else:
            if server_hostname:
                e = "server_hostname is for client-side only"
                raise ValueError(e)
            self.server_hostname = None
            self._client_unique = None
            self._server_unique = secrets.token_bytes(32)
            self._state = states.ServerStart(self)

    # ------------------------------------------------------------------
    # Public APIs
    # ------------------------------------------------------------------

    def initiate_connection(self):
        """
        Start the TLS three-way handshakes with the peer. Client-side it
        sends the first ClientHello message. Server-side it puts the
        connection in a state to accept the ClientHello.
        """
        if self.config.log_keys:
            is_key_logger_enabled = any(
                not isinstance(handler, logging.NullHandler)
                for handler in key_logger.handlers
            )
            if is_key_logger_enabled:
                logger.info("key log enabled for current connection.")
            else:
                logger.warning(
                    "key log was requested for current connection but no "
                    "logging.Handler seems setup on the %r logger. You must "
                    "setup one.\nlogging.getLogger(%r).addHandler(logging."
                    "FileHandler(path_to_keylogfile, %r))",
                    key_logger.name, key_logger.name, "w")

        self._state.initiate_connection()

    def receive_data(self, data: bytes) -> None:
        """
        Enqueue raw / encrypted data received from the peer inside the
        connection's buffer. Process the messages when enough data is
        present. Prepare the messages to be forwarded to this side's
        application upon next call to :meth:`data_to_read`, and the data
        to send to the peer upon next call to :meth:`data_to_send`.
        """
        if not data:
            e = "cannot receive empty data, use close_receiving_end() instead"
            raise ValueError(e)
        self._input_data += data

        while True:
            try:
                next_content = self._read_next_content()
                if not next_content:
                    break
                content_type, content_data = next_content
                content_type = try_cast(ContentType, content_type)
                content_name = content_type
                stream = TLSIO(content_data)
                try:
                    content = Content.get_parser(content_type).parse(
                        stream,
                        config=self.config,
                        nconfig=self.nconfig,
                    )
                    content_name = type(content).__name__
                    stream.ensure_eof()
                except TLSBufferError as exc:
                    raise alerts.DecodeError(*exc.args) from exc
                logger.debug("received %s", content_name)
                if content_type == ContentType.HANDSHAKE:
                    self._transcript.update(
                        content_data, self.config.other_side, content.msg_type
                    )
                self._state.process(content)
            except alerts.TLSFatalAlert as alert:
                self._fail(alert)
                raise
            except Exception:
                self._fail(alerts.InternalError())
                raise

        if self._cipher.should_rekey:
            self.rekey()

    def send_data(self, data: bytes):
        """
        Enqueue and encrypt clear/un-encrypted data comming from this
        side's application. Prepare the message to be send upon next
        call to :meth:`data_to_send`.
        """
        self._send_content(ApplicationData(data))

    def data_to_read(self, size=None) -> bytes:
        """
        Dequeue the clear data received from the peer that is intended
        for this side's application.

        It returns empty bytes when there is nothing to read, this is
        NOT an indication that the connection is closed.
        """
        if not self._application_data:
            return b''

        if size is None or size >= len(self._application_data):
            # optimization: don't copy the data
            application_data = self._application_data
            self._application_data = bytearray()
        else:
            application_data = self._application_data[:size]
            self._application_data = self._application_data[size:]
        return typing.cast('bytes', application_data)

    def data_to_send(self, size=None) -> bytes:
        """
        Dequeue the encrypted data that is intended to the peer.
        """
        if not self._output_data:
            return b''

        if size is None or size >= len(self._output_data):
            # optimization: don't copy the data
            output_data = self._output_data
            self._output_data = bytearray()
        else:
            output_data = self._output_data[:size]
            self._output_data = self._output_data[size:]
        return typing.cast('bytes', output_data)

    def rekey(self):
        if not self._state.can_send:
            e = f"cannot rekey in state {self._state.name()}"
            raise TLSError(e)
        raise NotImplementedError  # TODO

    def close_receiving_end(self):
        """
        Half-close the connection, ignore future incoming messages. Must
        be called when the TCP connection is closed.
        """
        if not self.is_post_handshake() or self.is_connected():
            self._fail()
            e = "the connection was gracelessly closed"
            raise RaggedEOF(e)
        if not isinstance(self._state, states.Closed):
            self._move_to_state(states.Closed)
        self._state.can_receive = False

    def close_sending_end(self):
        """
        Half-close the connection, signal the peer that this side will
        not send any new message.
        """
        if not isinstance(self._state, states.Closed | states.Failed):
            self._move_to_state(states.Closed)
        if self._state.can_send:
            self._send_content(alerts.CloseNotify())
            self._state.can_send = False

    def fail(self):
        """
        Signal the peer that an internal error occured, close both ends
        of the connection and ignore all future incomming messages.
        """
        self._fail(alerts.InternalError())

    def _fail(self, fatal_alert=None):
        if fatal_alert:
            if fatal_alert.level != AlertLevel.FATAL:
                e =("can only fail with a fatal alert which "
                    f"{fatal_alert!r} is not")
                raise ValueError(e)
            if self._state.can_send:
                self._send_content(fatal_alert)
        self._move_to_state(states.Failed)

    def is_post_handshake(self) -> bool:
        """
        True when the connection state is Connected / Closed (either
        end) / Failed; False otherwise.
        """
        return isinstance(self._state, states.Connected | states.Closed | states.Failed)

    def is_connected(self) -> bool:
        """
        True when the connection's state is Connected / Half-Closed
        (sending end), i.e. when we can still receive data from the
        peer; False otherwise.
        """
        if isinstance(self._state, states.Closed):
            # considere half-closed to be "connected" when it is still
            # ok to receive data
            return self._state.can_receive
        return isinstance(self._state, states.Connected)

    def wrap(self, tcp_socket: socket.socket) -> WrappedSocket:
        """ Bind this connection to a TCP socket and get a file-like interface. """
        return WrappedSocket(self, tcp_socket)

    # ------------------------------------------------------------------
    # Internal APIs
    # ------------------------------------------------------------------

    def _move_to_state(self, state_type, *args, **kwargs):
        self._state = state_type(self, *args, **kwargs)

    @property
    def max_fragment_length(self):
        if self.nconfig and self.nconfig.max_fragment_length is not None:
            return self.nconfig.max_fragment_length
        return self.config.max_fragment_length

    @property
    def max_record_length(self):
        return self.max_fragment_length + RECORD_HEADER_LENGTH + (
            256 if self._cipher.must_encrypt or self._cipher.must_decrypt else 0
        )

    def _read_next_record(self):
        while startswith_change_cipher_spec(self._input_data):
            self._input_data = self._input_data[6:]

        if len(self._input_data) < 5:  # noqa: PLR2004
            return None

        content_type, _legacy_version, content_length = \
            struct.unpack(RECORD_HEADER_STRUCT, self._input_data[:5])

        max_fragment_length = self.max_fragment_length
        if self._cipher.must_decrypt:
            max_fragment_length += 256
        if content_length > max_fragment_length:
            e =(f"the record is longer ({content_length} bytes) than "
                f"the allowed maximum ({max_fragment_length} bytes)")
            raise alerts.RecordOverFlow(e)

        if len(self._input_data) - 5 < content_length:
            return None

        header = self._input_data[:5]
        fragment = self._input_data[5:content_length + 5]
        self._input_data = self._input_data[content_length + 5:]
        if self._cipher.must_decrypt:
            if content_type == ContentType.APPLICATION_DATA:
                content_type, fragment = self._decrypt(header, fragment)
            elif content_type == ContentType.ALERT and not self.is_post_handshake():
                pass
            else:
                e = f"expected encrypted data but found clear {content_type}"
                raise alerts.UnexpectedMessage(e)

        if content_type == ContentType.CHANGE_CIPHER_SPEC:
            e = f"invalid {ContentType.CHANGE_CIPHER_SPEC} record"
            raise alerts.UnexpectedMessage(e)

        return content_type, fragment

    def _decrypt(self, header, fragment):
        innertext = self._cipher.decrypt(fragment, header)
        for i in range(len(innertext) -1, -1, -1):
            if innertext[i]:
                break
        else:
            e = "missing content type in encrypted record"
            raise alerts.UnexpectedMessage(e)
        return innertext[i], innertext[:i]

    def _read_next_content(self):
        if not self._input_handshake:
            record = self._read_next_record()
            if not record:
                return None

            content_type, fragment = record
            if content_type != ContentType.HANDSHAKE:
                return content_type, fragment

            self._input_handshake = fragment

        # Handshakes can be fragmented over multiple following records,
        # likewas a single record can holds multiple handshakes. Other
        # content types are subject to nor fragmentation nor coalescing.
        if len(self._input_handshake) < 4:  # noqa: PLR2004
            return None
        handshake_length = int.from_bytes(self._input_handshake[1:4], 'big')
        while len(self._input_handshake) - 4 < handshake_length:
            record = self._read_next_record()
            if not record:
                return None
            content_type, fragment = record
            if content_type != ContentType.HANDSHAKE:
                e =(f"expected {ContentType.HANDSHAKE} continuation record "
                    f"but {content_type} found")
                raise alerts.UnexpectedMessage(e)
            self._input_handshake += fragment

        content_data = self._input_handshake[:handshake_length + 4]
        self._input_handshake = self._input_handshake[handshake_length + 4:]
        return ContentType.HANDSHAKE, content_data

    def _send_content(self, content: Content):
        if (content.content_type == ContentType.APPLICATION_DATA
            and not self._state.can_send_application_data):
            e = f"cannot send application data in state {self._state.name()}"
            raise TLSError(e)
        if not self._state.can_send:
            e = f"cannot send content in state {self._state.name()}"
            raise TLSError(e)

        logger.debug("will send %s", type(content).__name__)
        data = content.serialize()  # type: ignore[attr-defined]

        if content.content_type == ContentType.HANDSHAKE:
            content = typing.cast('Handshake', content)
            self._transcript.update(data, self.config.side, content.msg_type)

        fragments: Iterable[bytes]
        if len(data) <= self.max_fragment_length:
            fragments = (data,)
        elif content.can_fragment:
            fragments = (
                data[i : i + self.max_fragment_length]
                for i in range(0, len(data), self.max_fragment_length)
            )
        else:
            e =(f"serialized {content} ({len(data)} bytes) doesn't fit "
                f"inside a single record (max {self.max_fragment_length}"
                " bytes and cannot be fragmented over multiple ones")
            raise ValueError(e)

        if self._cipher.must_encrypt:
            record_type = ContentType.APPLICATION_DATA
            # every fragment can be inflated by up to 256 bytes
            fragments = self._encrypt(
                content.content_type,
                fragments,
                self.max_fragment_length
            )
        else:
            record_type = content.content_type

        self._output_data += b''.join(
            b''.join([
                record_type.to_bytes(1, 'big'),
                TLSVersion.TLS_1_2.to_bytes(2, 'big'),  # legacy version
                len(fragment).to_bytes(2, 'big'),
                fragment,
            ])
            for fragment in fragments
        )

    def _encrypt(self, content_type, fragments, max_fragment_length):
        # RFC-8446 doesn't specify anything regarding padding, it only
        # says that it is a good idea. We add padding so that record
        # sizes are a multiple of 1kib (or less if max_fragment_length)
        chunk_size = min(max_fragment_length, 1024)

        for fragment in fragments:
            fragment_length = len(fragment) + 1 + self._cipher.tag_length
            padding = b'\x00' * (chunk_size - fragment_length % chunk_size)
            data = b''.join([
                fragment,
                content_type.to_bytes(1, 'big'),
                padding,
            ])
            header = b''.join([
                ContentType.APPLICATION_DATA.to_bytes(1, 'big'),
                TLSVersion.TLS_1_2.to_bytes(2, 'big'),  # legacy version
                (len(data) + self._cipher.tag_length).to_bytes(2, 'big'),
            ])
            encrypted_fragment = self._cipher.encrypt(data, header)

            yield encrypted_fragment
