from Crypto.Cipher import AES, PKCS1_OAEP
import os
import pyaes
import secrets
from base64 import b64decode
from base64 import b64encode
import sys
from Crypto.PublicKey import RSA
from binascii import hexlify
from datetime import datetime

class Hybrid_Key_Encryption :
    def __init__(self):
        self.plain_text = ""
        self.cipher_text = ""
        self.key = os.urandom(32)
        self.iv = secrets.randbits(256)
        private_key = RSA.generate(1024)
        public_key = private_key.publickey()
        self.private_key = private_key.export_key().decode()
        self.public_key = public_key.export_key().decode()
        self.encrypted_symmetric_key=""
        self.decrypted_symmetric_key =""

    def sender_encrypt(self):
        path = input('Enter the file path: ')
        start = datetime.now()
        with open(path, 'rb') as input_file:
            self.plain_text = input_file.read()
            aes = pyaes.AESModeOfOperationCTR(self.key, pyaes.Counter(self.iv))
            self.cipher_text = aes.encrypt(self.plain_text)
        self.encrypt_symmetric_key()
        end = datetime.now()
        print("Time taken to encrypt: "+ str(end-start))

    def encrypt_symmetric_key(self):
        cipher = PKCS1_OAEP.new(key=RSA.import_key(self.public_key))
        self.encrypted_symmetric_key = cipher.encrypt(self.key)

    def decrypt_symmetric_key(self):
        decrypt = PKCS1_OAEP.new(key=RSA.import_key(self.private_key))
        self.decrypted_symmetric_key = decrypt.decrypt(self.encrypted_symmetric_key)

    def receiver_decrypt(self):
        start =datetime.now()
        self.decrypt_symmetric_key()
        data = self.cipher_text
        aes = pyaes.AESModeOfOperationCTR(self.decrypted_symmetric_key, pyaes.Counter(self.iv))
        original_msg = aes.decrypt(data)
        end = datetime.now()
        print("Time taken to decrypt: "+ str(end-start))



# Driver program
if __name__ == "__main__":
    obj = Hybrid_Key_Encryption()
    obj.sender_encrypt()
    obj.receiver_decrypt()
