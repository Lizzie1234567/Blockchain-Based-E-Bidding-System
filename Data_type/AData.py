import time
import json
import hashlib
from model import Model
from database import *
from rpc import broadCast
from enum import Enum
from database import *
from CA_Sig.RSAED import *
from CA_Sig.Ecdsa import *

class AData():

    def __init__(self, CompanyName, msg, timestamp, credit: int = 0, datatype=0):
        self.CompanyName = CompanyName
        self.msg = msg
        self.timestamp = timestamp
        self.credit = credit
        self.datatype = datatype
        """
        class EnumDataType(int, Enum):
            AData: int = 0
            Tender_Data: int = 1
            Bidding_Data: int = 2
            AnonyWin_Data: int = 3
            Tender_Data: int = 4
        """

    #RSA加密CompanyName、msg
    def rsa_encryption(self):
        pk = PB_KeyDB.find_one()
        self.CompanyName = rsa_encrypt(pk, self.CompanyName)
        pk2 = PT_KeyDB.find_one()
        self.msg=rsa_encrypt(pk, self.msg)

    @classmethod
    def publish(cls, com_name, product, cre, dtype):
        e = Ecdsa.generate_keys()
        CompanyName = Ecdsa.sign_sig(com_name, e.sk)
        msg = Ecdsa.sign_sig(product, e.sk)
        credit = cre
        datatype = dtype
        dt = cls(CompanyName, msg, time.time(), credit, datatype)
        dt_dict = dt.to_dict()
        B_DataDB().insert(dt_dict)
        return dt_dict








    @property
    def get_hash(self):
        return hashlib.sha256((str(self.timestamp)+ str(self.CompanyName)+ str(self.credit)
                               + str(self.datatype)+ str(self.msg)).encode('utf-8')).hexdigest()



    @staticmethod
    def unblock_spread(undt):
        BroadCast().new_undata(undt)

    @staticmethod
    def blocked_spread(dts):
        BroadCast().blocked_datas(dts)

    def to_dict(self):
        return self.__dict__

