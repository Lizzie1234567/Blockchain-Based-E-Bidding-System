from Crypto.PublicKey import ECC
from database import PB_KeyDB
from database import SB_KeyDB
from database import PT_KeyDB
from database import ST_KeyDB


def G_K(self):
    # 生成并存储用于加密bidder信息的ECC对称密钥
    bkey = ECC.generate(curve='P-256')
    PK_bidding = bkey.public_key().export_key()
    SK_bidding = bkey.export_key()
    # 存入数据库
    pkdb = PB_KeyDB()
    pkdb.insert(PK_bidding)
    skdb = SB_KeyDB()
    skdb.insert(SK_bidding)

    # 生成并存储用于加密bidding product信息的ECC对称密钥
    tkey = ECC.generate(curve='P-256')
    PK_tender = tkey.public_key().export_key()
    SK_tender = tkey.export_key()
    pkdb2 = PT_KeyDB()
    pkdb2.insert(PK_tender)
    skdb2 = ST_KeyDB()
    skdb2.insert(SK_tender)




