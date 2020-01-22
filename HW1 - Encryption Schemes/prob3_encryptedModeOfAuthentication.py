from Crypto.Cipher import AES
import binascii, os
import sys

class Crypt_Schemes :
    def __init__(self):
        self.plain_text = ""
        self.key = os.urandom(32)

    def encrypt(self):
        aesCipher = AES.new(self.key, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(self.plain_text)
        self.cipher_text = (ciphertext, aesCipher.nonce, authTag)

    def print(self):
        print("CipherText: "+str(binascii.hexlify(self.cipher_text[0]).decode("utf8")))
        print("authTag: "+str(binascii.hexlify(self.cipher_text[2]).decode("utf8")))

    def verify_tag(self):
        cipher = input("Enter cipher text to be decrypted: ")
        cipherText = bytes.fromhex(str(cipher))
        (ciphertext, nonce, authTag) = self.cipher_text
        aesCipher = AES.new(self.key, AES.MODE_GCM, nonce)
        try:
            plain_text = aesCipher.decrypt_and_verify(cipherText, authTag)
            print(plain_text.decode("utf8"))
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
        0: obj.print(),
        3: cnt(),
        2: obj.verify_tag()
            }
    return switcher.get(argument, "Wrong input entered")

# Driver program
if __name__ == "__main__":
    print("1. Enter 1 to encrypt")
    print("2. Enter 2 to verify_tag")
    obj = Crypt_Schemes()
    argument=int(input())
    if argument==1:
            obj.plain_text = input("Enter input message to be encrypted: ").encode("utf8")
    crypt_functions(argument,obj)
