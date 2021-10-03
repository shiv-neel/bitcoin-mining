from hashlib import sha256
from datetime import date, datetime
import random

def hash(string):
    return sha256(string.encode('ascii')).hexdigest()

MAX_NONCE = 10000 # can be whatever integer your computational power can handle
def mine(block_number, transactions, prev_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    start = datetime.now()
    for nonce in range(MAX_NONCE):
        string = str(block_number) + transactions + prev_hash + str(nonce)
        new_hash = hash(string)
        if new_hash[0:prefix_zeros] == prefix_str:
            print(f'Successfuly mined bitcoin with nonce value {nonce}. Total duration: {datetime.now() - start}')
            return new_hash
    raise BaseException(f'Could not find hash after {MAX_NONCE} iterations. Total duration: {datetime.now() - start}')

if __name__ == '__main__':
    transactions = '''
    John_Doe->Jane_Smith->20,
    Kanye_West->Kendrick_Lamar->45
    '''
    difficulty = 20
    block_number = random.randint(500000)
    new_hash = mine(block_number, transactions, '348d77e943a990e64b08bd3bafc7c1b3fde497e92670f78cd8e9eb27529706f2', difficulty) # randomized prev hash
    print(new_hash)
