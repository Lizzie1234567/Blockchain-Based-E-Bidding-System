# miner


# coding:utf-8
from block import Block
import time
from database import BlockChainDB, DataDB, UnDataDB
from lib.common import unlock_sig, lock_sig
from Node import Node
# MAX_COIN = 21000000




class biddingUser(Node):
    def __int__(self,public_key: str =None,private_key: str = None,Etype: int = 3,address: str =None):
        self.public_key=public_key
        self.private_key=private_key
        self.Etype=Etype
        self.address=address



    def get_all_undata(self):
        UnDataDB().all_hashes()

    def create_account(self):
        pass

    def valid(self):
        pass

    def get_tx(self):
        pass

    def get_block(self):
        pass

    def get_blockchain(self):
        pass

    def broadcast_block(self):
        pass

