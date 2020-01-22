import hashlib as hasher
import datetime as date
import sys

class Block_Chain:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash

def find_hash(timestamp,data,previous_hash):
    sha = hasher.sha256()
    sha.update(str(timestamp).encode('utf-8') +
                str(data).encode('utf-8') +
                str(previous_hash).encode('utf-8'))
    return sha.hexdigest()

def add_block(prev_hash,message):
  timestamp = date.datetime.now()
  hash = find_hash(timestamp,str(message),prev_hash)
  return hash,timestamp

def verify_block_chain():
    count = 0
    input_file=open("ledger.txt",'r')
    for line in input_file:
        data_prev=line.split(',')
        if count==0: pass
        else:
            if find_hash(str(data_prev[2]),str(data_prev[0]),str(prev_hash)) != data_prev[1]:
                print('Data is tampered')
                sys.exit()
        prev_hash=data_prev[1]
        count+=1

verify_block_chain()

msg=input("Enter the transaction or message to be added to the ledger\n")
input_file=open("ledger.txt",'r')
lines=input_file.readlines()
prev_index=len(lines)-1
prev_line=lines[-1].split(",")
prev_hash= prev_line[1]
hash,time = add_block(prev_hash,msg)
with open("ledger.txt", "a") as original_file:
    original_file.write(str(msg)+','+str(hash)+','+str(time)+','+'\n')
