# snapshot.py
from .api import sj

def getSS(contracts: list):
        contractList = list(map(lambda x: sj.api.Contracts.Options[x], contracts))

        snapshots = sj.api.snapshots(contractList)
        # return snapshots[60]
        return [[i.code, i.close, i.buy_price, i.sell_price] for i in snapshots]
