# getPosition.py
from .snapshot import getSS


def getCurrentContractSS(positions: list):
    # code, last_price, pnl
    # print(positions[0].code, positions[0].last_price, positions[0].pnl)
    
    if len(positions) == 0:
        return ['   Hello  ' ,'I', 'am', 'Quagsire', None], ['   Hello  ' ,'I', 'am', 'Quagsire', None]
    
    if len(positions) == 1:
        if positions[0].code[-2] < 'M':
            
            return getSS([positions[0].code])[0] + [positions[0].pnl], ['   Hello  ' ,'I', 'am', 'Quagsire', None]
        else:
            return ['   Hello  ' ,'I', 'am', 'Quagsire', None], getSS([positions[0].code])[0] + [positions[0].pnl]
        
    if  positions[0].code[-2] < positions[1].code[-2]:
        return getSS([positions[0].code])[0] + [positions[0].pnl], getSS([positions[1].code])[0] + [positions[1].pnl]
    
    return getSS([positions[1].code])[0] + [positions[1].pnl], getSS([positions[0].code])[0] + [positions[0].pnl]

    # print(getSS([positions[0].code])[0] + [positions[0].pnl])
    # print(getSS([positions[1].code])[0] + [positions[1].pnl])
        
