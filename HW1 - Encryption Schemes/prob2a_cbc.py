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
        self.cipher_text = ""
        self.key = os.urandom(16)
        self.iv = get_random_bytes(AES.block_size)
        self.original_msg=""

    def encrypt(self):
        self.plain_text = input("Enter input message to be encrypted: ")
        self.cipher_text = AES.new(self.key, AES.MODE_CBC, self.iv)
        return b64encode(self.iv + self.cipher_text.encrypt(pad(self.plain_text.encode('utf-8'),AES.block_size)))


    def decrypt(self):
        cipherText = input("Enter cipher text to be decrypted: ")
        try:
            data = b64decode(cipherText)
            aes = AES.new(self.key,AES.MODE_CBC,data[:AES.block_size])
            original_msg =  unpad(aes.decrypt(data[AES.block_size:]), AES.block_size)
            self.originalMsg = os.urandom(len(self.plain_text))
            print("PlainText: " + original_msg.decode("utf8"))
        except:
            print("PlainText: Cipher changed, padding incorrect")

def cnt():
    arg = input("Press y/Y to continue decryption or n/N to exit: ")
    if arg=='y' or arg=="Y":
        pass
    else:
        sys.exit(0)

def crypt_functions(argument,obj):
    switcher = {
        1: print("CipherText: "+obj.encrypt().decode("utf8")),
        0: cnt(),
        2: obj.decrypt()
    }
    return switcher.get(argument, "Wrong input entered")

# Driver program
if __name__ == "__main__":
    print("1. Enter 1 to encrypt")
    print("2. Enter 2 to decrypt")
    obj = Crypt_Schemes()
    argument=int(input())
    crypt_functions(argument,obj)
