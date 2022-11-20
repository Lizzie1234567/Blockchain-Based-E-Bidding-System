import binascii
from abc import ABC
from enum import Enum
from typing import List
from Crypto.PublicKey import ECC


class ENodeType(int, Enum):
    UNDEFINED: int = 0
    BIDDINGUSER: int = 1
    TENDERUSER: int = 2
    SUPERVISOR: int = 3


class ANode(ABC):

    def __init__(self, private_key: ECC):
        self.blockchain = Blockchain.load_from_db() or Blockchain()
        self.private_key: ECC = private_key
        self.public_key: ECC = self.private_key.publickey()
        self.processed_hashes: List[str] = []

    @property
    def node_type(self) -> int:
        return ENodeType.UNDEFINED

    @property
    def identity(self) -> str:
        """
        ASCII Representation of node's public_key
        :return:
        """
        return binascii.hexlify(self.public_key.exportKey(format='DER')).decode('ascii')

    def __str__(self):
        return self.identity
