import time
import json
import hashlib
from model import Model
from database import DataDB, UnDataDB
from rpc import BroadCast
from enum import Enum
from database import PB_KeyDB,PT_KeyDB
from CA_Sig.RSAED import rsa_encrypt,rsa_decrypt
from CA_Sig.Ecdsa import Ecdsa







class AData():

    def __init__(self, CompanyName = None, NodeAddress=None,
                 msg="Nothing",credit: int = 0, datatype=0):
        self.CompanyName = CompanyName
        self.timestamp = int(time.time())
        self.msg = msg
        self.credit=credit
        self.datatype=datatype
        """
        class EnumDataType(int, Enum):
            AData: int = 0
            Tender_Data: int = 1
            Bidding_Data: int = 2
            AnonyWin_Data: int = 3
            Tender_Data: int = 4
        """


    @property
    def gen_hash(self):
        return hashlib.sha256((str(self.timestamp)+ str(self.CompanyName)+ str(self.credit)
                               + str(self.datatype)+ str(self.msg)).encode('utf-8')).hexdigest()


    @staticmethod
    def unblock_spread(undt):
        BroadCast().new_undata(undt)

    @staticmethod
    def blocked_spread(dts):
        BroadCast().blocked_datas(dts)

    def to_dict(self):
        dt = self.__dict__
        return dt


    #RSA加密CompanyName、msg
    def rsa_encryption(self):
        pk = PB_KeyDB.find_one()
        self.CompanyName = rsa_encrypt(pk, self.CompanyName)
        pk2 = PT_KeyDB.find_one()
        self.msg=rsa_encrypt(pk, self.msg)




