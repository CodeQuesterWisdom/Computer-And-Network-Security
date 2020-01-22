from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random
from binascii import hexlify
from datetime import datetime


class Public_Key_Encryption :
    def __init__(self):
        self.message = b"this is security course and public key encryption"
        private_key = RSA.generate(2048, Random.new().read)
        public_key = private_key.publickey()
        self.private_key = private_key
        self.public_key = public_key
        self.encrypted_file = 'encrypted_file.txt'

    def sender_encrypt(self):
        path = input('Enter the file path: ')
        size = 214
        start = datetime.now()
        with open(path, 'rb') as input_file:
            with open("encrypted_file", 'wb') as enc_file:
                while True:
                    text = input_file.read(size)
                    if len(text)==0: break
                    cipher = PKCS1_OAEP.new(key=self.public_key)
                    enc_file.write(cipher.encrypt(self.message))
        end = datetime.now()
        print("Time taken to encrypt: "+ str(end-start))

    def receiver_decrypt(self):
        start = datetime.now()
        size=256
        with open("encrypted_file", 'rb') as enc_file:
            with open("output.txt", 'wb') as dec_file:
                while True:
                    text = enc_file.read(size)
                    if len(text) == 0: break
                    decrypt = PKCS1_OAEP.new(key=self.private_key)
                    dec_file.write(decrypt.decrypt(text))
        end = datetime.now()
        print("Time taken to decrypt: "+ str(end-start))

# Driver program
if __name__ == "__main__":
    obj = Public_Key_Encryption()
    obj.sender_encrypt()
    obj.receiver_decrypt()
