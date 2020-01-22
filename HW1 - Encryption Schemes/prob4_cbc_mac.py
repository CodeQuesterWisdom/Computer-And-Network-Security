from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
from base64 import b64decode
from base64 import b64encode
import sys

class Crypt_Schemes :
    def __init__(self):
        self.plain_text = ""
        self.key1 = os.urandom(16)
        self.key2 = os.urandom(16)
        self.iv = bytes(16)
        self.tag=""

    def encrypt(self):
        aes = AES.new(self.key1, AES.MODE_CBC, self.iv)
        self.temp_cipher =  b64encode(self.iv + aes.encrypt(pad(self.plain_text.encode('utf-8'),AES.block_size)))
        tag = self.ecb_mode()
        return tag

    def pad_new(self,s,bs):
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs).encode()

    def ecb_mode(self):
        data = b64decode(self.temp_cipher)
        raw = self.pad_new(data,16)
        aes = AES.new(self.key2, AES.MODE_ECB)
        enc = aes.encrypt(raw)
        self.tag =  b64encode(enc).decode('utf-8')
        return self.tag

    def verify_tag(self):
        print("\nEnter input message and tag for verfication\n")
        self.plain_text = input("Enter input message: ")
        tag_old = input("Enter tag: ")
        tag_new = self.encrypt()
        if tag_old==tag_new:
            return "valid"
        else:
            return "invalid"

def cnt():
    arg = input("Press y/Y to continue decryption or n/N to exit: ")
    if arg=='y' or arg=="Y":
        pass
    else:
        sys.exit(0)

def crypt_functions(argument,obj):
    switcher = {
        1: print("AuthTag: "+ obj.encrypt()),
        0: cnt(),
        2: print(obj.verify_tag())
    }
    return switcher.get(argument, "Wrong input entered")

# Driver program
if __name__ == "__main__":
    print("1. Enter 1 to encrypt")
    print("2. Enter 2 to decrypt")
    obj = Crypt_Schemes()
    argument=int(input())
    if argument==1:
        obj.plain_text = input("Enter input message to be encrypted: ")
    crypt_functions(argument,obj)
