
from Node import Node


class tenderUser(Node):
    def __int__(self,public_key: str =None,private_key: str = None,Etype: int = 2,address: str =None):
        self.public_key=public_key
        self.private_key=private_key
        self.address=address
        self.Etype=Etype




    def get_block(self):
        pass

    def get_blockchain(self):
        pass

    def broadcast_tx(self):
        pass