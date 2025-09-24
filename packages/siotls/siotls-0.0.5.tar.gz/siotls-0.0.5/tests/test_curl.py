import dataclasses
import logging
import os
import re
import shutil
import unittest
from collections import namedtuple
from os import fspath
from threading import Thread

from parameterized import parameterized  # type: ignore[import-untyped]

from siotls import TLSConnection
from siotls.crypto import TLSKeyExchange
from siotls.examples.simple_server import make_http11_response
from siotls.iana import NamedGroup

from . import TAG_INTEGRATION, NetworkMixin, TestCase, test_temp_dir
from .config import server_config

CURL_PATH = shutil.which('curl')

logger = logging.getLogger(__name__)
curl_logger = logger.getChild('curl')


def fix_curl_log(message):
    # might be a nice first contribution to cURL...
    return message.replace(
        "TLS header, Finished (20)", "TLS header, Change Cipher Spec (20)"
    ).replace(
        "TLS header, Unknown (21)", "TLS header, Alert (21)"
    ).replace(
        "TLS header, Certificate Status (22)", "TLS header, Handshake (22)"
    ).replace(
        "TLS header, Supplemental data (23)", "TLS header, Application Data (23)"
    )


@unittest.skipUnless(TAG_INTEGRATION, "enable with SIOTLS_INTEGRATION=1")
@unittest.skipUnless(CURL_PATH, "curl not found in path")
class TestCURL(NetworkMixin, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.keylogfile = (test_temp_dir / 'keylogfile.txt').open('w+')
        cls.addClassCleanup(cls.keylogfile.close)
        cls.curl_pipe_r, cls.curl_pipe_w = os.pipe()
        cls.addClassCleanup(os.close, cls.curl_pipe_r)
        cls.addClassCleanup(os.close, cls.curl_pipe_w)
        Thread(target=cls.run_curl_logging, args=(curl_logger,)).start()

    def setUp(self):
        super().setUp()
        self.keylogfile.seek(0)
        self.keylogfile.truncate()

    @classmethod
    def run_curl_logging(cls, curl_logger):
        curl_log_re = re.compile(r'^(?:(\*)|== (\w+):) ', re.MULTILINE)
        buffer = ""
        while True:
            try:
                read = os.read(cls.curl_pipe_r, 1024).decode(errors='ignore')
            except OSError:
                break
            *messages, buffer = curl_log_re.split(buffer + read)
            for message, group1, group2 in zip(it:=iter(messages), it, it, strict=True):
                if not message:
                    continue
                level_name = 'INFO' if group1 else group2.upper()
                curl_logger.log(
                    logging._nameToLevel[level_name],
                    fix_curl_log(message.rstrip())
                )

    def curl(
        self,
        version='1.3',
        max_time=1,
        tls_max='1.3',
        options=None,
    ):
        args = [
            CURL_PATH, f'https://{self.host}:{self.port}',
            '--no-progress-meter',
            '--cacert', fspath(test_temp_dir.joinpath('ca-cert.pem')),
        ]

        loglevel = logger.getEffectiveLevel()
        if loglevel <= logging.DEBUG:
            args.extend(['--trace-ascii', '-'])
        elif loglevel <= logging.INFO:
            args.append('--verbose')
        elif loglevel <= logging.WARNING:
            pass
        elif loglevel <= logging.ERROR:
            args.append('--show-error')
        else:
            args.append('--silent')

        if version:
            args.append(f'--tlsv{version}')
        if max_time is not None:
            args.append('--max-time')
            args.append(str(max_time))
        if tls_max is not None:
            args.append('--tls-max')
            args.append(tls_max)
        for option, value in (options or {}).items():
            args.append(f'--{option}')
            args.append(value)
        env = {'SSLKEYLOGFILE': self.keylogfile.name}
        proc = self.popen(
            args,
            stdout=self.curl_pipe_w,
            stderr=self.curl_pipe_w,
            env=env,
        )

        client, client_info = self.socket.accept()
        self.addCleanup(client.close)

        return proc, client

    @parameterized.expand([
        ('server_hello', NamedGroup.x25519),
        ('hello_retry_request', NamedGroup.x448),
    ])
    def test_curl_keylogfile(self, _, group):
        if group not in TLSKeyExchange:
            self.skipTest("incompatible crypto backend")

        KeyLogFormat = namedtuple("KeyLogFormat", ["label", "client_random", "value"])

        config = dataclasses.replace(
            server_config,
            key_exchanges=[group],
            alpn=[b'http/1.1'],
            log_keys=True
        )
        conn =  TLSConnection(config)
        proc, client = self.curl()

        with self.assertLogs('siotls.keylog', level='INFO') as logs:  # noqa: SIM117
            with conn.wrap(client) as sclient:
                http_get = sclient.read()
                self.assertEqual(
                    http_get.partition(b'\r\n')[0],
                    b"GET / HTTP/1.1"
                )
                sclient.write(make_http11_response(204, ""))

        client.close()
        proc.wait(timeout=1)

        siotls_keylog = [
            KeyLogFormat(*line.rpartition(':')[2].split(' '))
            for line in logs.output
            if '#' not in line
        ]

        curl_keylog = [
            KeyLogFormat(*line.strip().split(' '))
            for line in self.keylogfile.readlines()
            if not line.startswith('#')
        ]

        # Validate labels
        self.assertEqual(
            sorted({log.label for log in siotls_keylog}),
            sorted([log.label for log in siotls_keylog]),
            "There must not be any duplicated label in siotls keylog"
        )
        self.assertEqual(
            sorted({log.label for log in curl_keylog}),
            sorted([log.label for log in curl_keylog]),
            "There must not be any duplicated label in curl keylog"
        )

        # Validate client randoms
        self.assertEqual(
            [log.client_random for log in siotls_keylog],
            [conn._client_unique.hex()] * len(siotls_keylog),
            "All key logs are for the same client siotls side",
        )
        self.assertEqual(
            [log.client_random for log in curl_keylog],
            [conn._client_unique.hex()] * len(curl_keylog),
            "All key logs are for the same client curl side",
        )

        # Validate secret values
        siotls_keylog = {label: value for label, _, value in siotls_keylog}
        curl_keylog = {label: value for label, _, value in curl_keylog}
        self.assertEqual(set(siotls_keylog), set(curl_keylog))
        self.assertEqual(siotls_keylog, curl_keylog)
