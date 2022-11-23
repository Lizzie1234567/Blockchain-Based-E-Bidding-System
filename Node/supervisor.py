#miner



# coding:utf-8
from block import Block
import time
from data import Vout, Data
from account import get_account
from database import BlockChainDB, DataDB, UnDataDB
from lib.common import unlock_sig, lock_sig

MAX_COIN = 21000000
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


def get_all_undata():
    UnDataDB().all_hashes()


def mine():
    """
    Main miner method.
    """
    # Found last block and unchecked datas.
    last_block = BlockChainDB().last()
    if len(last_block) == 0:
        last_block = coinbase().to_dict()
    untxdb = UnDataDB()
    # Miner reward
    rw = reward()
    untxs = untxdb.find_all()
    untxs.append(rw.to_dict())
    # untxs_dict = [untx.to_dict() for untx in untxs]
    untx_hashes = untxdb.all_hashes()
    # Clear the undata database.
    untxdb.clear()

    # Miner reward is the first data.
    untx_hashes.insert(0, rw.hash)
    cb = Block(last_block['index'] + 1, int(time.time()), untx_hashes, last_block['hash'])
    nouce = cb.pow()
    cb.make(nouce)
    # Save block and data to database.
    BlockChainDB().insert(cb.to_dict())
    DataDB().insert(untxs)
    # Broadcast to other nodes
    Block.spread(cb.to_dict())
    Data.blocked_spread(untxs)
    return cb
