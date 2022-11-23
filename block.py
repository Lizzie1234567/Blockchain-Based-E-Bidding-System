# coding:utf-8

from model import Model
from rpc import BroadCast
from Dhash import Dhash


class Block(Model):

    def __init__(self, index, timestamp, data, preHash, Btype):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.preHash = preHash
        self.Btype = Btype
        self.hash = ''

    def header_hash(self):
        """
        Refer to bitcoin block header hash
        """
        return Dhash.Dhash(str(self.index) + str(self.timestamp) + str(self.data) + str(self.preHash) + self.Btype)


    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, bdict):
        b = cls(bdict['index'], bdict['timestamp'], bdict['data'], bdict['preHash'], bdict['type'])
        b.hash = bdict['hash']
        b.nouce = bdict['nouce']
        return b

    @staticmethod
    def spread(block):
        BroadCast().new_block(block)




