# coding:utf-8
from PoA import PoA
from model import Model
from rpc import BroadCast
from CA_Sig.Dhash import Dhash
from CA_Sig.Dhash import Dhash


class Block(Model):

    def __init__(self, index, timestamp, data, preHash, Btype=0):
        self.index = index
        self.timestamp = timestamp
        self.data: list = data
        self.preHash = preHash
        self.Btype = Btype
        self.hash = ""
        self.miner = PoA()

    def get_hash(self):
        self.hash = Dhash.Dhash(str(self.index) + str(self.timestamp) + str(self.data) + str(self.preHash) + self.Btype)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, bdict):
        b = cls(bdict['index'], bdict['timestamp'], bdict['data'], bdict['preHash'], bdict['Btype'])
        b.hash = bdict['hash']
        b.miner = bdict['miner']
        return b

    @staticmethod
    def spread(block):
        BroadCast().new_block(block)
