from Crypto.PublicKey import ECC
from Crypto.Cipher import PKCS1_v1_5
import base64


# Use ECC public key to encrypt the message
def ecc_encrypt(pk, plain):
    #
    key = ECC.import_key(pk)
    ecc = PKCS1_v1_5.new(key)
    cipher = ecc.encrypt(plain)
    return base64.b64encode(cipher)


# Use ECC private key to decrypt the message
def ecc_decrypt(sk, cipher2):
    key2 = ECC.import_key(sk)
    ecc2 = PKCS1_v1_5.new(key2)
    plain2 = ecc2.decrypt(base64.b64decode(cipher2), 'ERROR')
    return plain2
