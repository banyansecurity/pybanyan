import fnmatch
from typing import Optional, List

from cryptography import x509
from cryptography.hazmat.primitives.serialization import load_pem_private_key
# noinspection PyUnresolvedReferences
from cryptography.x509.oid import NameOID, ExtensionOID


class CertPair:
    def __init__(self, cert_filename: str, key_filename: str):
        self._cert_file = cert_filename
        self._key_file = key_filename
        with open(self._cert_file, 'rt') as f:
            self._cert = x509.load_pem_x509_certificate(f.read().encode('ascii'))
        with open(self._key_file, 'rt') as f:
            self._key = load_pem_private_key(f.read().encode('ascii'), None)

    def get_common_name(self) -> Optional[str]:
        cn = self._cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        if cn:
            return cn[0].value
        return None

    def get_san_dns_names(self) -> List[str]:
        try:
            san: x509.SubjectAlternativeName = self._cert.extensions.get_extension_for_oid(
                ExtensionOID.SUBJECT_ALTERNATIVE_NAME).value
            return san.get_values_for_type(x509.DNSName)
        except x509.extensions.ExtensionNotFound:
            return list()

    def get_names(self) -> List[str]:
        domains = [self.get_common_name()]
        domains.extend(self.get_san_dns_names())
        return domains

    def is_name_match(self, name: str) -> bool:
        for candidate in self.get_names():
            if name == candidate:
                return True
            if '*' in candidate and fnmatch.fnmatch(name, candidate):
                return True
        return False
