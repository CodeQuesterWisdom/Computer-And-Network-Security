import hashlib
import random
import multiprocessing
import threading
import numpy
import sys

def findNonce1():
    nonce = 0
    nonce = numpy.int64(nonce)
    print(type(nonce))
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 922337203685477580:break
            nonce+=1
zzz
def findNonce2():
    nonce = 9223372036854775807
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 1844674407370955160:break
            nonce+=1

def findNonce3():
    nonce = 1844674407370955160
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 2767011611056432740:break
            nonce+=1

def findNonce4():
    nonce = 2767011611056432740
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 3689348814741910320:break
            nonce+=1

def findNonce5():
    nonce = 3689348814741910320
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 4611686018427387900:break
            nonce+=1

def findNonce6():
    nonce = 4611686018427387900
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 5534023222112865480:break
            nonce+=1

def findNonce7():
    nonce = 5534023222112865480
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 6456360425798343060:break
            nonce+=1

def findNonce8():
    nonce = 6456360425798343060
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 7378697629483820640:break
            nonce+=1

def findNonce9():
    nonce = 7378697629483820640
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 8301034833169298220:break
            nonce+=1

def findNonce10():
    nonce = 8301034833169298220
    nonce = numpy.int64(nonce)
    while True:
        noncedData =  str(nonce) + "sunayanavempati"
        hash = hashlib.sha256(noncedData.encode('utf-8')).hexdigest()
        #hashlib requires data to be encoded before hashed.
        if hash.startswith ("000000000"):
            print([nonce,hash])
            system.exit(0)
            return
        else:
            if nonce > 9223372036854775807:break
            nonce+=1


p1= threading.Thread(target=findNonce1)
p2= threading.Thread(target=findNonce2)
p3= threading.Thread(target=findNonce3)
p4= threading.Thread(target=findNonce4)
p5= threading.Thread(target=findNonce5)
p6= threading.Thread(target=findNonce6)
p7= threading.Thread(target=findNonce7)
p8= threading.Thread(target=findNonce8)
p9= threading.Thread(target=findNonce9)
p10= threading.Thread(target=findNonce10)
p1.start()
print("finding in block 1")
p2.start()
print("finding in block 2")
p3.start()
print("finding in block 3")
p4.start()
print("finding in block 4")
p5.start()
print("finding in block 5")
p6.start()
print("finding in block 6")
p7.start()
print("finding in block 7")
p8.start()
print("finding in block 8")
p9.start()
print("finding in block 9")
p10.start()
print("finding in block 10")
