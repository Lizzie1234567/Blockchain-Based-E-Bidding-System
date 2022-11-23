# miner


# coding:utf-8
from block import Block
import time
from data import Vout, Data
from account import get_account
from database import BlockChainDB, DataDB, UnDataDB
from lib.common import unlock_sig, lock_sig
from Node import Node
# MAX_COIN = 21000000


# REWARD = 20


# def reward():
#     reward = Vout(get_account()['address'], REWARD)
#     tx = Data([], reward)
#     return tx


# def coinbase():
#     """
#     First block generate.
#     """
#     rw = reward()
#     cb = Block(0, int(time.time()), [rw.hash], "")
#     nouce = cb.pow()
#     cb.make(nouce)
#     # Save block and datas to database.
#     BlockChainDB().insert(cb.to_dict())
#     DataDB().insert(rw.to_dict())
#     return cb

class biddingUser(Node):
    def __int__(self,public_key: str =None,private_key: str = None,Etype: int = 3):
        self.public_key=public_key
        self.private_key=private_key
        self.Etype=Etype



    def get_all_undata(self):
        UnDataDB().all_hashes()

    def create_account(self):
        pass

    def valid(self):
        pass

    def get_tx(self):
        pass

    def get_block(self):

    def get_blockchain(self):
        pass

    def broadcast_block(self):
        pass

