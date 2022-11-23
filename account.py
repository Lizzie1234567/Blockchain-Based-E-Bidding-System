# coding:utf-8
import hashlib
import lib.common
from model import Model
from lib.common import pubkey_to_address
from database import S_AccountDB
from database import T_AccountDB
from database import B_AccountDB


def S_account():
    private_key = lib.common.random_key()
    public_key = lib.common.hash160(private_key.encode())
    address = pubkey_to_address(public_key.encode())
    adb = S_AccountDB()
    adb.insert({'pubkey': public_key, 'address': address})
    return private_key, public_key, address


def T_account():
    private_key = lib.common.random_key()
    public_key = lib.common.hash160(private_key.encode())
    address = pubkey_to_address(public_key.encode())
    adb = T_AccountDB()
    adb.insert({'pubkey': public_key, 'address': address})
    return private_key, public_key, address


def B_account():
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



