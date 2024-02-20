from Backtestprice import csv_price
from SimpleMovingAverage import SimpleMovingAverage
from BollingerBands import BollingerBands
from Algorithm import Algorithm
from BuyOrSell import Action
from CandleStick_Indicator import CandleStick
from Price_Lister import Price_Lister
from ExponentialMovingAverage import ExponentialMovingAverage
from RelativeStrengthIndex import RelativeStrengthIndex
from AccessToken import AccessToken
import requests
from Account import Account
from APIprice import Price
from Counter import Counter
import time
from datetime import datetime
import csv
from datetime import date
from BuyOrSell import BuyOrSell
#objects
TICKER = 'NVDA'

AccessTokenObject = AccessToken()
AccountObject = Account()
ActionObject = BuyOrSell(TICKER)
PriceObject = Price()
PriceListerObject = Price_Lister()
CounterObject = Counter()
AlgorithmObject = Algorithm()
ExponentialMovingAverageObject = ExponentialMovingAverage()

#constant variables

TICKER = 'NVDA'
TIME_BETWEEN_PRICES = 5

#actual code

def main():
    now = datetime.now()
    access_token = AccessTokenObject.main()
    price = PriceObject.get_price(access_token, TICKER)
    AccountObject.get_account_data(access_token)
    PriceListerObject.prev_price_lister(price)
    count = CounterObject.main()

    with open("databases/backtest_data{}.csv".format(date.today()), 'a', newline='') as backtest_data:
        csv_writer = csv.writer(backtest_data, delimiter=',')
        csv_writer.writerow([price])

    prev_12_prices = PriceListerObject.return_prev_12_prices()
    prev_26_prices = PriceListerObject.return_prev_26_prices()
    prev_20_prices = PriceListerObject.return_prev_20_prices()
    prev_53_prices = PriceListerObject.return_prev_53_prices()

    if count > 54:

        AlgorithmObject.set_indicators(price,prev_12_prices,prev_26_prices, prev_53_prices, prev_20_prices, count)
        AlgorithmObject.triple_EMA_crossover()

        buy_state = AlgorithmObject.return_buy_state()
        sell_state = AlgorithmObject.return_sell_state()
        wait_state = AlgorithmObject.return_do_nothing()
        holding_stock = AlgorithmObject.return_holding_stock()

        if wait_state == True:
            pass
        elif buy_state == True:
            ActionObject.buy(access_token, price, TICKER)
        elif sell_state == True:
            ActionObject.sell(access_token, price)
        else:
            pass

        AlgorithmObject.reset()
    else:
        pass

    if now.minute == 59 and now.hour == 12 and holding_stock == True:
        ActionObject.sell(access_token, price)





def timer():
    while True:
        tic = time.perf_counter()
        now = datetime.now()
        SIX_THIRTY_AM = now.replace(hour=6, minute=30)
        ONE_PM = now.replace(hour=13, minute=0)

        if now > SIX_THIRTY_AM and now < ONE_PM and now.day != 5 and now.day != 6:

            main()
            print(now)
            print("--------------------")

            toc = time.perf_counter()
            action_time = toc - tic

            try:
                time.sleep(TIME_BETWEEN_PRICES - action_time)
            except ValueError:
                pass
        else:
            print(now)
            toc = time.perf_counter()
            time.sleep(60)




timer()

