import time
import json
import hashlib
from model import Model
from database import DataDB, UnDataDB
from rpc import broadCast
from enum import Enum


class EnumNodeType(int, Enum):
    supervisor: int = 0
    tenderUser: int = 1
    biddingUser: int = 2


class ANode():
    def __int__(self, public_key: str = None, private_key: str = None, Etype: int = 1, address: str = None):
        self.public_key = public_key
        self.private_key = private_key
        self.address = address
        self.Etype = Etype






    @staticmethod
    def unblock_spread(undt):
        broadCast().new_undata(undt)

    @staticmethod
    def blocked_spread(dts):
        broadCast().blocked_datas(dts)

    def to_dict(self):
        dt = self.__dict__
        return dt


