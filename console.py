# coding:utf-8
from account import *
from miner import mine
from rpc import get_clients, BroadCast, start_server
from data import *
from database import *
from block import *
from PoA import *
import sys
import multiprocessing
import rpc
from node import *
from lib.common import cprint
import inspect
from Data_type.AData import *

MODULES = ['account', 'tx', 'blockchain', 'miner', 'node']


def upper_first(string):
    return string[0].upper() + string[1:]


class Node():

    def add(self, args):
        add_node(args[0])
        rpc.BroadCast().add_node(args[0])
        cprint('Allnode', get_nodes())

    def run(self, args):
        start_node(args[0])

    def list(self, args):
        for t in NodeDB().find_all():
            cprint('Node', t)


class Miner():
    def start(self, args):
        if get_S_account() == None:
            cprint('ERROR', 'Please create account before start miner.')
            exit()
        start_node(args[0])
        while True:
            print('Miner new block')
            mine()



class Account():
    def createS(self,args):

        ac = S_account()

        cprint('Private Key', ac[0])
        cprint('Public Key', ac[1])
        cprint('Address', ac[2])

    def createT(self,args):

        ac = T_account()

        cprint('Private Key', ac[0])
        cprint('Public Key', ac[1])
        cprint('Address', ac[2])

    def createB(self,args):

        ac = B_account()

        cprint('Private Key', ac[0])
        cprint('Public Key', ac[1])
        cprint('Address', ac[2])

    def get(self, args):
        cprint('All Account', S_account().read())

    def current(self, args):
        cprint('Current Account', get_S_account())


class Blockchain():

    def list(self, args):
        for t in BlockChainDB().find_all():
            cprint('Blockchain', str(t))


class Tx():

    def list(self, args):
        for t in DataDB().find_all():
            cprint('Data', t)

    def publish(self, args):
        dt = AData.publish(args[0], args[1], args[2], args[3])
        print(AData.unblock_spread(dt))
        cprint('Data publish', dt)


def usage(class_name):
    module = globals()[upper_first(class_name)]
    print('  ' + class_name + '\r')
    print('    [action]\r')
    for k, v in module.__dict__.items():
        if callable(v):
            print('      %s' % (k,))
    print('\r')


def help():
    print("Usage: python console.py [module] [action]\r")
    print('[module]\n')
    for m in MODULES:
        usage(m)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        help()
        exit()
    module = sys.argv[1]
    if module == 'help':
        help()
        exit()
    if module not in MODULES:
        cprint('Error', 'First arg shoud in %s' % (str(MODULES, )))
        exit()
    mob = globals()[upper_first(module)]()
    method = sys.argv[2]
    # try:
    getattr(mob, method)(sys.argv[3:])
    # except Exception as e:
    #     cprint('ERROR','/(ㄒoㄒ)/~~, Maybe command params get wrong, please check and try again.')
