# order.py
import shioaji
from .api import sj
import time

class OrderBot:
        
    def sellNowOrder(self, contractCode :str):
        order = sj.api.Order(
            action=shioaji.constant.Action.Sell,
            price=1000,
            quantity=1,
            price_type=shioaji.constant.FuturesPriceType.MKP,
            order_type=shioaji.constant.OrderType.FOK, 
            octype=shioaji.constant.FuturesOCType.New,
            account=sj.api.futopt_account
        )
        contract = sj.api.Contracts.Options[contractCode]
        # print(f'contract -> {contract}')
        trade = sj.api.place_order(contract, order)
        print(f'trade -> {trade.status.status}')
        print(f'trade -> {trade.status.deals}')
        print(f'trade -> {type(trade.status.deals)}')
        
    def ClosePosition(self, contractCode :str):
        order = sj.api.Order(
            action=shioaji.constant.Action.Buy,
            price=1,
            quantity=1,
            price_type=shioaji.constant.FuturesPriceType.MKP,
            order_type=shioaji.constant.OrderType.FOK, 
            octype=shioaji.constant.FuturesOCType.Cover,
            account=sj.api.futopt_account
        )
        contract = sj.api.Contracts.Options[contractCode]

        trade = sj.api.place_order(contract, order)
        time.sleep(3)
        print(trade)
    
    def test(self, contractCode :str):
        order = sj.api.Order(
            action=shioaji.constant.Action.Buy,
            price=1,
            quantity=1,
            price_type=shioaji.constant.FuturesPriceType.LMT,
            order_type=shioaji.constant.OrderType.ROD, 
            octype=shioaji.constant.FuturesOCType.Auto,
            account=sj.api.futopt_account
        )
        contract = sj.api.Contracts.Options[contractCode]

        trade = sj.api.place_order(contract, order)
        time.sleep(3)
        print(f'trade -> {trade.status.status}')
        print(f'trade -> {trade.status.deals}')
        print(f'trade -> {type(trade.status.deals)}')
        time.sleep(30)

    def adjustOrder(self, oldContract, NewContract):
        self.ClosePosition(oldContract)
        self.sellNowOrder(NewContract)
        
