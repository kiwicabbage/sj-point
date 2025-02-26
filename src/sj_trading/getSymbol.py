# getSymbol.py
import datetime

# select the put and call contracts in string format
def selectContract(sj):

       all_contract = [i for i in (sj.api.Contracts.Options) if 
              str(i)[:2] == "TX"]
       # get begin symbol code

       BegCode = str(all_contract[0])[:3]
       contractList = all_contract[0]

       if BegCode == 'TX4' and str(all_contract[1])[:3] == 'TXO':
              BegCode = 'TXO'
              contractList = all_contract[1]

       elif BegCode == 'TX1' and str(all_contract[1])[:3] == 'TX5':
              BegCode = 'TX5'
              contractList = all_contract[1]
       elif BegCode == 'TX1' and str(all_contract[1])[:3] == 'TX4':
              BegCode = 'TX4'
              contractList = all_contract[1]
              
       elif BegCode == 'TX1' and str(all_contract[1])[:3] == 'TX3':
              BegCode = 'TX3'
              contractList = all_contract[1]
       print(f'Nearest Contracts is {BegCode}')

       # now = datetime.datetime.now()
       for i in contractList:
              month = int(i.delivery_month[-2:])
              year = i.delivery_month[:-2]

              break
       
       EndCodeC = (chr(month + 64) + year[-1])
       EndCodeP = (chr(month + 76) + year[-1])
       print(EndCodeC, EndCodeP)

       StrikePrices = (sorted([int(i.code[3:-2]) for i in contractList if i.code[-2:] == EndCodeP 
              and i.code[:3] == BegCode]))


       CallContracts = ([BegCode + str(i) + EndCodeC for i in StrikePrices])
       PutContracts = ([BegCode + str(i) + EndCodeP for i in StrikePrices])
       # print(API.api.Contracts.Options[contracts[9]])
       return CallContracts, PutContracts

# use the contracts to get the snapshot
# snapshot return the buy price and the contract code


# def getEndCode()