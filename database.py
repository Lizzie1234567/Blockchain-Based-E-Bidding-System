# coding:utf-8
import json
import os

BASEDBPATH = 'data'
BLOCKFILE = 'blockchain'
TXFILE = 'tx'
UNTXFILE = 'untx'
S_ACCOUNTFILE = 'S_account'
T_ACCOUNTFILE = 'T_account'
B_ACCOUNTFILE = 'B_account'

SK_BIDDINGFILE = 'SK_bidding'
PK_BIDDINGFILE = 'PK_bidding'
SK_TENDERFILE = 'SK_tender'
PK_TENDERFILE = 'PK_tender'

NODEFILE = 'node'

class BaseDB():

    filepath = ''

    def __init__(self):
        self.set_path()
        self.filepath = '/'.join((BASEDBPATH, self.filepath))

    def set_path(self):
        pass

    def find_all(self):
        return self.read()

    def insert(self, item):
        self.write(item)  

    def read(self):
        raw = ''
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath,'r+') as f:
            raw = f.readline()
        if len(raw) > 0:
            data = json.loads(raw)
        else:
            data = []
        return data

    def write(self, item):
        data = self.read()
        if isinstance(item,list):
            data = data + item
        else:
            data.append(item)
        with open(self.filepath,'w+') as f:
            f.write(json.dumps(data))
        return True

    def clear(self):
        with open(self.filepath,'w+') as f:
            f.write('')

    def hash_insert(self, item):
        exists = False
        for i in self.find_all():
            if item['hash'] == i['hash']:
                exists = True
                break
        if not exists:
            self.write(item)  

class NodeDB(BaseDB):

    def set_path(self):
        self.filepath = NODEFILE  


class S_AccountDB(BaseDB):
    def set_path(self):
        self.filepath = S_ACCOUNTFILE

    def find_one(self):
        ac = self.read()
        return ac[0]

class T_AccountDB(BaseDB):
    def set_path(self):
        self.filepath = T_ACCOUNTFILE

    def find_one(self):
        ac = self.read()
        return ac[0]

class B_AccountDB(BaseDB):
    def set_path(self):
        self.filepath = B_ACCOUNTFILE

    def find_one(self):
        ac = self.read()
        return ac[0]

class PB_KeyDB(BaseDB):
    def set_path(self):
        self.filepath = PK_BIDDINGFILE

    def find_one(self):
        ac = self.read()
        return ac[0]

class SB_KeyDB(BaseDB):
    def set_path(self):
        self.filepath = SK_BIDDINGFILE

    def find_one(self):
        ac = self.read()
        return ac[0]

class PT_KeyDB(BaseDB):
    def set_path(self):
        self.filepath = PK_TENDERFILE

    def find_one(self):
        ac = self.read()
        return ac[0]

class ST_KeyDB(BaseDB):
    def set_path(self):
        self.filepath = SK_TENDERFILE

    def find_one(self):
        ac = self.read()
        return ac[0]


class BlockChainDB(BaseDB):

    def set_path(self):
        self.filepath = BLOCKFILE

    def last(self):
        bc = self.read()
        if len(bc) > 0:
            return bc[-1]
        else:
            return []

    def find(self, hash):
        one = {}
        for item in self.find_all():
            if item['hash'] == hash:
                one = item
                break
        return one

    def insert(self, item):
        self.hash_insert(item)

class DataDB(BaseDB):
    """
    Datas that save with blockchain.
    """
    def set_path(self):
        self.filepath = TXFILE

    def find(self, hash):
        one = {}
        for item in self.find_all():
            if item['hash'] == hash:
                one = item
                break
        return one

    def insert(self, txs):
        if not isinstance(txs,list):
            txs = [txs]
        for tx in txs:
            self.hash_insert(tx)

class UnDataDB(DataDB):
    """
    Datas that doesn't store in blockchain.
    """
    def set_path(self):
        self.filepath = UNTXFILE

    def all_hashes(self):
        hashes = []
        for item in self.find_all():
            hashes.append(item['hash'])
        return hashes