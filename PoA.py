from database import S_AccountDB
import random


def PoA() -> str:
    sadb = S_AccountDB()
    validators = sadb.find_all()
    if len(validators) == 0:
        return False
    validator = random.choice(validators)
    validator_address = validator['address']

    return validator_address
