import base64
import requests
from time import sleep
import binascii
import sys

class Crypt_Schemes :
    def __init__(self):
        self.plain_text = ""
        self.cipher_text = ""
        self.key = ""
        self.original_msg=""
        #self.url = "https://api.random.org/json-rpc/2/basic?num=1&len="+str(len(self.plain_text))+"&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new"
        #https://www.random.org/strings/
    def get_key(self,l):
        response = requests.get("https://api.random.org/json-rpc/2/basic?num=1&len="+str(l)+"&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new")
        if response.status_code == 200:
            self.key = response.text.strip()
        else:
            print("Request to random.org failed, retrying...")
            sleep(5)
            self.get_key()
        return self.key

    def encrypt(self):
        self.plain_text = input("Enter input message to be encrypted: ")
        self.key = self.get_key(len(self.plain_text))
        for v,k in zip(self.plain_text,self.key):
            self.cipher_text += chr(ord(v) ^ ord(k))
        print("CipherText: "+str(binascii.hexlify(self.cipher_text.encode("utf8")).decode("utf8")))

    def decrypt(self):
        cipher_text = input("Enter cipher text to be decrypted: ")
        try:
            cipherText = bytes.fromhex(str(cipher_text))
            for v,k in zip(cipherText,self.key):
                self.original_msg += chr(ord(chr(v)) ^ ord(k))
            print("PlainText: "+self.original_msg)
        except:
            print("invalid")


def cnt():
    arg = input("Press y/Y to continue decryption or n/N to exit: ")
    if arg=='y' or arg=="Y":
        pass
    else:
        sys.exit(0)

def crypt_functions(argument,obj):
    switcher = {
        1: obj.encrypt(),
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
