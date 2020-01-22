from Crypto.Cipher import AES
import os
import pyaes
import secrets
from base64 import b64decode
from base64 import b64encode
import sys

class Crypt_Schemes :
    def __init__(self):
        self.plain_text = ""
        self.cipher_text = ""
        self.key = os.urandom(32)
        self.iv = secrets.randbits(256)

    def encrypt(self):
        self.plain_text = input("Enter input message to be encrypted: ")
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
        self.cipher_text = aes.encrypt(self.plain_text)
        return b64encode(self.cipher_text)


    def decrypt(self):
        cipher_text = input("Enter cipher text to be decrypted: ")
        data = b64decode(cipher_text)
        aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
        original_msg = aes.decrypt(data)
        return original_msg

def cnt():
    arg = input("Press y/Y to continue decryption or n/N to exit: ")
    if arg=='y' or arg=="Y":
        pass
    else:
        sys.exit(0)

def crypt_functions(argument,obj):
    switcher = {
        1: print("CipherText: "+ obj.encrypt().decode("utf8")),
        0: cnt(),
        2: print("PlainText: "+ obj.decrypt().decode("utf8"))
    }
    return switcher.get(argument, "Wrong input entered")

# Driver program
if __name__ == "__main__":
    print("1. Enter 1 to encrypt")
    print("2. Enter 2 to decrypt")
    obj = Crypt_Schemes()
    argument=int(input())
    crypt_functions(argument,obj)
