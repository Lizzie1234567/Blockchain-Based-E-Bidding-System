from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


# Use RSA public key to encrypt the message
def rsa_encrypt(pk, plain):
    #
    key = RSA.import_key(pk)
    rsa = PKCS1_v1_5.new(key)
    cipher = rsa.encrypt(plain)
    return base64.b64encode(cipher)


# Use RSA private key to decrypt the message
def rsa_decrypt(sk, cipher2):
    key2 = RSA.import_key(sk)
    rsa2 = PKCS1_v1_5.new(key2)
    plain2 = rsa2.decrypt(base64.b64decode(cipher2), 'ERROR')
    return plain2
