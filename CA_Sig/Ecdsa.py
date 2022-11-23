from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS


class Ecdsa:

    def __init__(self, sk = None, pk = None):
        self.sk = sk
        self.pk = pk

    def generate_keys(self):
        key = ECC.generate(curve='p-256')
        self.sk = key.export_key(format='PEM')
        self.pk = key.public_key().export_key(format='PEM')
        return key

    @staticmethod
    def sign_sig(message, sk):
        signer = DSS.new(sk, 'fips-186-3')
        hasher = SHA256.new(message.encode())
        sig = signer.sign(hasher)
        return sig

    @staticmethod
    def verify_sig(message2, pk, sig2):
        verifier = DSS.new(pk, 'fips-186-3')
        hasher2 = SHA256.new(message2.encode())
        try:
            verifier.verify(hasher2, sig2)
            return 0
        except ValueError:
            return 1
