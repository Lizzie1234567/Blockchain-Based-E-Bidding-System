# coding:utf-8
import hashlib

import const
import lib.common
from model import Model
from lib.common import pubkey_to_address
from database import S_AccountDB
from database import T_AccountDB
from database import B_AccountDB
from const import Const
from CA_Sig import Ecdsa


def S_account():
    Const.Permission_Level = 0
    private_key = lib.common.random_key()
    public_key = lib.common.hash160(private_key.encode())


    address = pubkey_to_address(public_key.encode())
    adb = S_AccountDB()
    adb.insert({'pubkey': public_key, 'address': address})
    return private_key, public_key, address


def T_account():
    Const.Permission_Level = 1
    private_key = lib.common.random_key()
    public_key = lib.common.hash160(private_key.encode())
    address = pubkey_to_address(public_key.encode())
    adb = T_AccountDB()
    adb.insert({'pubkey': public_key, 'address': address})
    return private_key, public_key, address


def B_account():
    Const.Permission_Level = 2
    private_key = lib.common.random_key()
    public_key = lib.common.hash160(private_key.encode())
    address = pubkey_to_address(public_key.encode())
    adb = B_AccountDB()
    adb.insert({'pubkey': public_key, 'address': address})
    return private_key, public_key, address

def get_S_account():
    adb = S_AccountDB()
    return adb.find_one()

def get_T_account():
    adb = T_AccountDB()
    return adb.find_one()

def get_B_account():
    adb = B_AccountDB()
    return adb.find_one()



