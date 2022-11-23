# coding:utf-8
from block import Block
import time
from Data_type import AData
from database import *
from lib.common import cprint


def coinbase():
    """
    First block generate.
    """
    dt = AData('first', 'first', 100, 0)
    cb = Block(0, int(time.time()), dt, [dt.get_hash], 1)
    # Save block and transactions to database.
    BlockChainDB().insert(cb.to_dict())
    DataDB().insert(dt.to_dict())
    return cb


def get_all_undatas():
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
    # untxs_dict = [untx.to_dict() for untx in untxs]
    # Clear the untransaction database.
    untxdb.clear()
    lb = last_block['index']
    """
    class EnumDataType(int, Enum):
        AData: int = 0
        Tender_Data: int = 1
        Bidding_Data: int = 2
        AnonyWin_Data: int = 3
        Tender_Data: int = 4
    """
    if Tender_Data_list:
        lb = lb + 1
        cb = Block(lb, int(time.time()), Tender_Data_list, last_block['hash'], 1)
        cb.get_hash()
        BlockChainDB().insert(cb.to_dict())
        Block.spread(cb.to_dict())
        cprint('Miner new block', cb.to_dict())
    elif Bidding_Data_list:
        lb = lb + 1
        cb = Block(lb, int(time.time()), Bidding_Data_list, last_block['hash'], 2)
        cb.get_hash()
        BlockChainDB().insert(cb.to_dict())
        Block.spread(cb.to_dict())
        cprint('Miner new block', cb.to_dict())
    elif AnonyWin_Data_list:
        lb = lb + 1
        cb = Block(lb, int(time.time()), AnonyWin_Data_list, last_block['hash'], 3)
        cb.get_hash()
        BlockChainDB().insert(cb.to_dict())
        Block.spread(cb.to_dict())
        cprint('Miner new block', cb.to_dict())
    elif PublicWin_Data_list:
        lb = lb + 1
        cb = Block(lb, int(time.time()), PublicWin_Data_list, last_block['hash'], 4)
        cb.get_hash()
        BlockChainDB().insert(cb.to_dict())
        Block.spread(cb.to_dict())
        cprint('Miner new block', cb.to_dict())

    # Save block and transactions to database.

    DataDB().insert(untxs)
    # Broadcast to other nodes
    AData.blocked_spread(untxs)


