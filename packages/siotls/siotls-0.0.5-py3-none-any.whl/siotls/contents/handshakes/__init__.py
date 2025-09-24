import dataclasses
import textwrap
import typing

from siotls.contents import alerts
from siotls.iana import ContentType, HandshakeType, HandshakeType_
from siotls.language import Serializable
from siotls.utils import RegistryMeta

from .. import Content  # noqa: TID252


@dataclasses.dataclass(init=False)
class Handshake(Content, Serializable):
    """
    Abstract base class and registry for :class:`siotls.iana.HandshakeType`.
    """
    _registry_key = '_handshake_registry'
    _handshake_registry: typing.ClassVar = {}

    content_type = ContentType.HANDSHAKE
    can_fragment = True

    _struct = textwrap.dedent("""
        struct {
            HandshakeType msg_type;    /* handshake type */
            uint24 length;             /* remaining bytes in message */
            select (Handshake.msg_type) {
                case 0x01: ClientHello;
                case 0x02: ServerHello;
                case 0x04: EndOfEarlyData;
                case 0x05: EncryptedExtensions;
                case 0x08: CertificateRequest;
                case 0x0b: Certificate;
                case 0x0d: CertificateVerify;
                case 0x0f: Finished;
                case 0x14: NewSessionTicket;
                case 0x18: KeyUpdate;
            };
        } Handshake;
    """).strip('\n')

    msg_type: HandshakeType | HandshakeType_ = dataclasses.field(repr=False)
    """ The unique numeric identifier of the handshake. """

    def __init_subclass__(cls, *, register=True, **kwargs):
        super().__init_subclass__(**kwargs)
        if register and Handshake in cls.__bases__:
            cls._handshake_registry[cls.msg_type] = cls

    @classmethod
    def parse(abc, stream, **kwargs):
        msg_type = stream.read_int(1)
        length = stream.read_int(3)
        try:
            cls = abc[HandshakeType(msg_type)]
        except ValueError as exc:
            raise alerts.IllegalParameter(*exc.args) from exc
        with stream.limit(length):
            return cls.parse_body(stream, **kwargs)

    def serialize(self):
        msg_data = self.serialize_body()
        return b''.join([
            self.msg_type.to_bytes(1, 'big'),
            len(msg_data).to_bytes(3, 'big'),
            msg_data,
        ])


from .certificate import CertificateHandshake
from .certificate_request import CertificateRequest
from .certificate_verify import CertificateVerify
from .client_hello import ClientHello
from .encrypted_extensions import EncryptedExtensions
from .end_of_early_data import EndOfEarlyData
from .finished import Finished
from .key_update import KeyUpdate
from .new_session_ticket import NewSessionTicket
from .server_hello import HelloRetryRequest, ServerHello
