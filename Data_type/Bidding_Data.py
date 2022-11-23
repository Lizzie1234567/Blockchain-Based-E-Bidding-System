import base64
import binascii
import collections

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey
from werkzeug.datastructures import FileStorage
import time
import json
import hashlib
from model import Model
from database import DataDB, UnDataDB
from rpc import BroadCast
from enum import Enum
from .AData import EnumDataType, AData


class Bidding_Data(AData):

    def __init__(self, CompanyName: str = None, NodeAddress=None, msg="Nothing", signature: str = None):
        self.CompanyName = CompanyName
        self.NodeAddress = NodeAddress
        self.timestamp = int(time.time())
        self.msg = msg
        self.signature = signature
        self.hash = self.gen_hash()
        self.datatype = self.data_type()

    @property
    def data_type(self) -> int:
        return EnumDataType.Date_Transfer

    def gen_hash(self):
        return hashlib.sha256((str(self.timestamp) + str(self.CompanyName) + str(self.signature)
                               + str(self.NodeAddress) + str(self.msg)).encode('utf-8')).hexdigest()

    @staticmethod
    def unblock_spread(undt):
        BroadCast().new_undata(undt)

    @staticmethod
    def blocked_spread(dts):
        BroadCast().blocked_datas(dts)

    def to_dict(self):
        dt = self.__dict__
        return dt
