from Backtestprice import csv_price
from SimpleMovingAverage import SimpleMovingAverage
from BollingerBands import BollingerBands
from Algorithm import Algorithm
from BuyOrSell import Backtest_Action
from CandleStick_Indicator import CandleStick
from Price_Lister import Price_Lister
from ExponentialMovingAverage import ExponentialMovingAverage
from RelativeStrengthIndex import RelativeStrengthIndex
from Counter import Counter
import _csv
import csv


class Backtest:
    def __init__(self):
        self.total_money_made = 0
        self.count = 0
        self.should_buy = False
        self.should_sell = False
        self.macd_object=ExponentialMovingAverage()
        self.historgram=None
        self.stock_state=False
        self.overall_money_made=0
        self.overall_held_money_made=0
    def main(self):
        for self.month in range(6,13):
            if self.month<10:
                self.month='0{}'.format(self.month)
            for self.day in range(32):
                if self.day<10:
                    self.day = '0{}'.format(self.day)
                csv_file_name = 'databases/backtest_data2021-{month}-{day}.csv'.format(month=self.month, day=self.day)
                print(csv_file_name)
                self.total_money_made = 0
                self.count = 0
                self.should_buy = False
                self.should_sell = False
                self.algorithm_object=Algorithm()
                self.prev_price_lister_object=Price_Lister()

                self.counter_object=Counter()
                self.stock_state = False
                try:
                    with open(csv_file_name) as f:
                        self.list_length=sum(1 for line in f)
                    with open(csv_file_name, 'r') as price_history:
                        self.csv_reader = csv.reader(price_history, delimiter=',')
                        try:
                            for line in self.csv_reader:
                                self.count = self.counter_object.main()
                                #self.list_length=len(self.csv_reader)
                                try:
                                    self.price = line[0]
                                except IndexError:
                                    break
                                self.price=float(self.price)
                                if self.count==1:
                                    self.first_price=self.price
                                elif self.count==self.list_length:
                                    self.last_price=self.price

                                self.prev_price_lister_object.prev_price_lister(self.price)

                                self.prev_12_prices = self.prev_price_lister_object.return_prev_12_prices()
                                self.prev_26_prices = self.prev_price_lister_object.return_prev_26_prices()
                                self.prev_20_prices = self.prev_price_lister_object.return_prev_20_prices()
                                self.prev_53_prices = self.prev_price_lister_object.return_prev_53_prices()
                                if self.count>54:
                                    self.algorithm_object.set_indicators(self.price, self.prev_12_prices, self.prev_26_prices,
                                                                   self.prev_53_prices, self.prev_20_prices, self.count)
                                    self.total_money_made,self.trades_completed=self.algorithm_object.triple_EMA_crossover()
                                if self.count==self.list_length:
                                    self.overall_money_made +=self.total_money_made
                                    self.overall_held_money_made +=(self.last_price-self.first_price)
                                    print(f'''
date:{csv_file_name}
money made if stock was bought and held: {self.last_price-self.first_price}
money made with algorithm: {self.total_money_made}
trades completed: {self.trades_completed}
overall money made held: {self.overall_held_money_made}
overall money made algo: {self.overall_money_made}
------------------
                                    ''')
                        except _csv.Error:
                            break

                except FileNotFoundError:
                    print('file not found')
                    pass
                finally:
                    del self.algorithm_object
                    del self.prev_price_lister_object

                    del self.counter_object




'''
class Backtest():
    def __init__(self, file, moneyMade, holdingAction):

        self.price_getter = csv_price(file)
        self.price = self.price_getter.get_csv_price()
        if self.price == False:
            

        self.SMA_object = SimpleMovingAverage(self.price)
        self.BollingerBands_object = BollingerBands()
        self.Algorithm_object = Algorithm()
        self.Action_object = Backtest_Action(self.price)
        self.CandleStickObject = CandleStick()
        self.Price_Lister_object = Price_Lister()
        self.Exponential_Moving_Average_Object = ExponentialMovingAverage()
        self.RelativeStrengthIndex_Object = RelativeStrengthIndex()
        self.moneyMade = moneyMade
        self.holdingAction = holdingAction
    def algorithm(self):
        while True:
            try:
                self.price = self.price_getter.get_csv_price()
                self.count = self.price_getter.counter()
                self.prev_20_values = self.SMA_object.return_prev_20_values()
                self.Price_Lister_object.prev_price_lister(self.price)
                self.prev_12_prices = self.Price_Lister_object.return_prev_12_prices()
                self.prev_26_prices = self.Price_Lister_object.return_prev_26_prices()
                self.prev_20_prices = self.Price_Lister_object.return_prev_20_prices()
                self.prev_53_prices = self.Price_Lister_object.return_prev_53_prices()

                if self.count >= 54:
                    self.Algorithm_object.set_indicators(self.price, self.prev_12_prices,self.prev_26_prices, self.prev_53_prices, self.prev_20_prices, self.count)
                    self.Algorithm_object.triple_EMA_crossover()

                    self.sell_state = self.Algorithm_object.return_sell_state()
                    self.buy_state = self.Algorithm_object.return_buy_state()
                    self.wait_state = self.Algorithm_object.return_do_nothing()

                    if self.wait_state:
                        pass
                    elif self.sell_state == True:
                        self.Action_object.sell(self.price)

                    elif self.buy_state == True:
                        self.Action_object.buy(self.price)

                    else:
                        print("what the fuck ay yo man what the fuck what da faaaaaaaaaaaaaaack")

                    self.Algorithm_object.reset()
                else:
                    pass



            except:
                self.moneyMade += self.Action_object.return_money_made()
                self.holdingAction += self.Action_object.return_holding_action()
                return self.moneyMade, self.holdingAction
                break
moneyMade = 0
holdingAction = 0
for month in range(6,13):
    if month<10:
        month='0{}'.format(month)
    for day in range(1,32):
        if day<10:
            day = '0{}'.format(day)
        file = 'databases/backtest/backtest_data2021-{month}-{day}.csv'.format(month=month, day=day)
        Backtester = Backtest(file, moneyMade, holdingAction)
        moneyMade, holdingAction = Backtester.algorithm()
'''
backtest_object = Backtest()
backtest_object.main()