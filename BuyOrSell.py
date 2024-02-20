import math
from config import account_id
import requests
class Backtest_Action:
    def __init__(self, price):
        self.buying_power = 2000 #change this later
        self.price = 0
        self.first_price = price
        self.stock_holdings = 0
        self.stocks_to_buy = 2
        self.status = 0
    def buy(self, price):
        self.price = price
        self.stocks_to_buy = math.floor(self.buying_power/self.price)
        self.buying_power = self.buying_power - self.stocks_to_buy*self.price
        self.bought_price = self.price
        self.stock_holdings += self.stocks_to_buy
        print("total balance:" , self.buying_power)
        print("price bought:" , price)
        print("stocks bought:", self.stocks_to_buy)

        print("--------------")


    def sell(self, price):
        self.price = price
        self.stocks_to_sell = self.stock_holdings
        self.buying_power = self.buying_power + (self.stocks_to_sell * self.price)
        self.stock_holdings -= self.stocks_to_sell
        print("total:" , self.buying_power)
        print("price:" , price)
        print("money made:", self.buying_power - 2000)
        print("holding_action (average):", self.price * self.stocks_to_buy - self.first_price * self.stocks_to_buy)
        print("Stock price action:", self.price - self.first_price)
        print("profit on trade: ",self.price-self.bought_price )
        print("price bought:", self.bought_price)

        print("percentage:", ((self.buying_power/2000) - 1)*100)
        print("--------------")
        return self.buying_power-2000, self.price*self.stocks_to_buy - self.first_price * self.stocks_to_buy
    def return_money_made(self):
        return self.buying_power - 2000
    def return_holding_action(self):
        return self.price * self.stocks_to_buy - self.first_price * self.stocks_to_buy
    def return_profits(self):
        return self.buying_power
class BuyOrSell:
    def __init__(self,symbol):
        self.symbol=symbol
        self.current_buying_power=0
        self.stocks_to_buy=0.0
        self.status=0
        self.total_money_made=0

        self.endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/orders".format(account_id)
    def main(self, price, should_buy, should_sell,access_token,account_id,cash_balance):
        self.price=price
        self.cash_balance=cash_balance
        self.access_token=access_token
        self.header={'Authorization':"Bearer {}".format(self.access_token),
                     "Content-Type":"application/json"}
        self.endpoint=r"https://api.tdameritrade.com/v1/accounts/{}/orders".format(account_id)
        if should_buy:
            self.buy()
            #self.test()
        elif should_sell:
            self.sell()
            #self.test()
        else:
            pass
    def buy(self, access_token, price, TICKER):
        self.symbol = TICKER
        self.access_token = access_token
        self.price = price
        self.header={'Authorization':"Bearer {}".format(self.access_token),
                     "Content-Type":"application/json"}

        self.current_buying_power=1000
        self.stocks_to_buy = math.floor(self.current_buying_power / self.price)
        self.count = 0
        payload={'orderType':'MARKET',
                      'session':'NORMAL',
                      'duration':'DAY',
                      'orderStrategyType':'SINGLE',
                      'orderLegCollection':[{'instruction':'Buy',
                                             'quantity':self.stocks_to_buy,
                                             'instrument':{'symbol':'{}'.format(self.symbol),'assetType':'EQUITY'}}]}

        #rs.orders.order_buy_fractional_by_quantity(self.symbol, self.stocks_to_buy, timeInForce='gfd', extendedHours=False)
        while self.status != 200 and self.status != 201 and self.count <3:
            self.count += 1
            self.content=requests.post(url=self.endpoint,json=payload,headers=self.header)
            self.status=self.content.status_code

            print(self.status)

        self.status=0
        self.stock_holdings = self.stocks_to_buy
        #print(content.status_code)
        print('''
                -------------------------------------------
                 ------> {} stock(s) bought at ${} <------
                -------------------------------------------
                '''.format(self.stock_holdings, self.price))
        self.bought_price = self.price

    def sell(self, access_token, price):
        self.access_token = access_token
        self.price = price
        self.header={'Authorization':"Bearer {}".format(self.access_token),
                     "Content-Type":"application/json"}
        self.count = 0
        payload = {'orderType': 'MARKET',
                        'session': 'NORMAL',
                        'duration': 'DAY',
                        'orderStrategyType': 'SINGLE',
                        'orderLegCollection': [{'instruction': 'Sell',
                                                'quantity': self.stocks_to_buy,
                                                'instrument': {'symbol': '{}'.format(self.symbol),
                                                               'assetType': 'EQUITY'}}]}
        while self.status != 200 and self.status != 201 and self.count<3:
            try:
                self.count+=1
                self.content = requests.post(url=self.endpoint, json=payload, headers=self.header)
                self.status = self.content.status_code
            except:
                pass
            print(self.status)
            print(self.content)
            print('''
            -----------------------------------
            {} stock(s) sold at ${}
            Bought stock at ${}
            Made ${} on trade
            -----------------------------------
    
            '''.format(self.stock_holdings, self.price, self.bought_price,
                       (self.price - self.bought_price) * self.stock_holdings))
            self.total_money_made += self.price-self.bought_price
            print("Total Money Made: ", self.total_money_made)


class Action:
    def __init__(self):
        self.buying_power = 1000
        self.price = 0
        self.stock_holdings = 0
        self.stocks_to_buy = 0
        self.status = 0
        self.bought_price = 0
    def buy(self, access_token, price):
        self.status = 0
        self.price = price
        self.stocks_to_buy = math.floor(self.buying_power/self.price)
        self.count =0
        endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/orders".format(account_id)
        header = {'Authorization':'Bearer {}'.format(access_token),
                  'Content-Type':'application/json'}
        payload = {
            "orderType": "MARKET",
            "session": "NORMAL",
            "duration": "DAY",
            "orderStrategyType": "SINGLE",
            "orderLegCollection": [
                {
                    "instruction": "Buy",
                    "quantity": self.stocks_to_buy,
                    "instrument": {
                        "symbol": "NVDA",
                        "assetType": "EQUITY"
                    }
                }
            ]
        }
        while self.status != 200 and self.status != 201 and self.count < 3:
            self.count +=1
            self.content = requests.post(url=endpoint,json=payload,headers=header)
            self.status = self.content.status_code
        self.bought_price = self.price
        self.stock_holdings = self.stocks_to_buy
        print('''
        -------------------------------------------
         ------> {} stock(s) bought at ${} <------
        -------------------------------------------
        '''.format(self.stock_holdings,self.price))
        print(self.content)
        print(self.status)

    def sell(self, access_token, price):
        self.price = price
        self.status = 0
        self.count = 0
        endpoint = r"https://api.tdameritrade.com/v1/accounts/{}/orders".format(account_id)
        header = {'Authorization': 'Bearer {}'.format(access_token),
                  'Content-Type': 'application/json'}
        payload = {
            "orderType": "MARKET",
            "session": "NORMAL",
            "duration": "DAY",
            "orderStrategyType": "SINGLE",
            "orderLegCollection": [
                {
                    "instruction": "Sell",
                    "quantity": self.stock_holdings,
                    "instrument": {
                        "symbol": "NVDA",
                        "assetType": "EQUITY"
                    }
                }
            ]
        }
        while self.status != 200 and self.status != 201 and self.count <3:
            self.count += 1
            self.content = requests.post(url=endpoint, json=payload, headers=header)
            self.status = self.content.status_code
        print('''
        -----------------------------------
        {} stock(s) sold at ${}
        Bought stock at ${}
        Made ${} on trade
        -----------------------------------
        
        '''.format(self.stock_holdings, self.price, self.bought_price, (self.price-self.bought_price)*self.stock_holdings))
        print(self.content)
        print(self.status)