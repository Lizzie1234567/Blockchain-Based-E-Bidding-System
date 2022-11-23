import time
import json
import hashlib
from model import Model
from database import DataDB, UnDataDB
from rpc import BroadCast
from enum import Enum

class EnumDataType(int, Enum):
    Date_Transfer: int = 0
    Tender_Data: int = 1
    Bidding_Data: int = 2
    AnonyWin_Data: int = 3
    Tender_Data: int = 4


class AData():

    def __init__(self, CompanyName: str = None, NodeAddress=None, msg="Nothing", signature: str = None):
        self.CompanyName = CompanyName
        self.NodeAddress= NodeAddress
        self.timestamp = float(time.time())
        self.msg = msg
        self.signature = signature
        self.hash = self.gen_hash()
        self.datatype=self.data_type()

    @property
    def data_type(self) -> int:
        return EnumDataType.Date_Transfer

    def gen_hash(self):
        return hashlib.sha256((str(self.timestamp)+ str(self.CompanyName)+ str(self.signature)
                               + str(self.NodeAddress)+ str(self.msg)).encode('utf-8')).hexdigest()

    @classmethod
    def transfer(cls, from_addr, to_addr, amount):
        if not isinstance(amount, int):
            amount = int(amount)

        # ready_utxo, change = select_outputs_greedy(unspents, amount)
        print('ready_utxo', ready_utxo[0].to_dict())
        vin = ready_utxo
        vout = []
        vout.append(Vout(to_addr, amount))
        vout.append(Vout(from_addr, change))
        tx = cls(vin, vout)
        tx_dict = tx.to_dict()
        UnDataDB().insert(tx_dict)
        return tx_dict

    @staticmethod
    def unblock_spread(undt):
        BroadCast().new_undata(undt)

    @staticmethod
    def blocked_spread(dts):
        BroadCast().blocked_datas(dts)

    def to_dict(self):
        dt = self.__dict__
        if not isinstance(self.vin, list):
            self.vin = [self.vin]
        if not isinstance(self.vout, list):
            self.vout = [self.vout]
        dt['vin'] = [i.__dict__ for i in self.vin]
        dt['vout'] = [i.__dict__ for i in self.vout]
        return dt


    def select_outputs_greedy(unspent, min_value):
        if not unspent: return None
        # 分割成两个列表。
        lessers = [utxo for utxo in unspent if utxo.amount < min_value]
        greaters = [utxo for utxo in unspent if utxo.amount >= min_value]
        key_func = lambda utxo: utxo.amount
        greaters.sort(key=key_func)
        if greaters:
            # 非空。寻找最小的greater。
            min_greater = greaters[0]
            change = min_greater.amount - min_value
            return [min_greater], change
        # 没有找到greaters。重新尝试若干更小的。
        # 从大到小排序。我们需要尽可能地使用最小的输入量。
        lessers.sort(key=key_func, reverse=True)
        result = []
        accum = 0
        for utxo in lessers:
            result.append(utxo)
            accum += utxo.amount
            if accum >= min_value:
                change = accum - min_value
                return result, change
                # 没有找到。
        return None, 0
