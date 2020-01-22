from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import PKCS1_v1_5

class Digital_Signature:
    def __init__(self):
        random_generator = Random.new().read
        key = RSA.generate(2048, random_generator)
        self.private_key = key.exportKey()
        self.public_key = key.publickey().exportKey()

    def generate_signature(self,data):
        signer = PKCS1_v1_5.new(RSA.importKey(self.private_key))
        digest = SHA256.new()
        digest.update(data)
        self.sig = signer.sign(digest)
        print()
        print("Signature: ")
        print(self.sig)
        print("")
        print("Public/Verification key : "+ str(self.public_key))
        print("")

    def verify_signature(self,data, public_key, signature):
        if not (str(self.public_key)==public_key): return False
        verifier = PKCS1_v1_5.new(RSA.importKey(self.public_key))
        digest1 = SHA256.new()
        digest1.update(data)
        if str(self.sig) == signature:
            return verifier.verify(digest1, self.sig)
        else:
            return False
            #return public_key.verify(data, signature)


# Driver program
if __name__ == "__main__":
    obj = Digital_Signature()
    path = input('Enter the file path: ')
    with open(path, 'rb') as input_file:
        msg = input_file.read()
    obj.generate_signature(msg)

    print("For verification: ")
    path = input('Enter the file path: ')
    print()
    sign = input("Enter signature: ")
    print()
    key = input("Enter Verification Key: ")
    print()
    with open(path, 'rb') as input_file:
        msg = input_file.read()
    if obj.verify_signature(msg, key, sign): print("Valid")
    else: print("Invalid")
