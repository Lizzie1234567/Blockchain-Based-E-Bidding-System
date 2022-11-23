# coding:utf-8
from block import Block
import time
from Data_type import AData
from account import *
from database import *
from lib.common import unlock_sig, lock_sig

MAX_COIN = 21000000
REWARD = 20


def coinbase():
    """
    First block generate.
    """
    cb = Block(0, int(time.time()), '', "")
    # Save block and transactions to database.
    BlockChainDB().insert(cb.to_dict())
    return cb


def get_all_untransactions():
    UnDataDB().all_hashes()


def mine():
    """
    Main miner method.
    """
    # Found last block and unchecked transactions.
    last_block = BlockChainDB().last()
    if len(last_block) == 0:
        last_block = coinbase().to_dict()
    untxdb = UnDataDB()
    untxs = untxdb.find_all()

    Tender_Data_list = []
    Bidding_Data_list = []
    AnonyWin_Data_list = []
    PublicWin_Data_list = []

    """
           class EnumDataType(int, Enum):
               AData: int = 0
               Tender_Data: int = 1
               Bidding_Data: int = 2
               AnonyWin_Data: int = 3
               PublicWin_Data: int = 4
           """

    for i in untxs:
        if i.datatype == 1:
            Tender_Data_list.append(i)
        elif i.datatype == 2:
            Bidding_Data_list.append(i)
        elif i.datatype == 3:
            AnonyWin_Data_list.append(i)
        elif i.datatype == 4:
            PublicWin_Data_list.append(i)

    a = AData.AData()
    untxs.append(a.to_dict())
    # untxs_dict = [untx.to_dict() for untx in untxs]
    untx_hashes = untxdb.all_hashes()
    # Clear the untransaction database.
    untxdb.clear()
    # Miner reward is the first transaction.
    cb = Block(last_block['index'] + 1, int(time.time()), untx_hashes, last_block['hash'])
    # Save block and transactions to database.
    BlockChainDB().insert(cb.to_dict())
    DataDB().insert(untxs)
    # Broadcast to other nodes
    Block.spread(cb.to_dict())
    a.blocked_spread(untxs)
    return cb
