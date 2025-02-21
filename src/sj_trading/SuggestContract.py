from .snapshot import getSS



def findContracts(snapshot, target = 20):
    # [[i.code, i.close, i.buy_price, i.sell_price], ...]
    # buy_price -> int, sell_price -> int
    # the above is the format of the contract
    # the target is the target price
    # snapshot = getSS(Contracts)
    
    closest_index, closest_value = max(
        ((index, value[2]) for index, value in enumerate(snapshot) 
            if value[2] < target),
        key=lambda x: x[1],
        default=(None, None)
    )

    # return the shioaji contract type
    return snapshot[closest_index]
    

