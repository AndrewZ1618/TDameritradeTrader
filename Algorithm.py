from Backtestprice import csv_price
from SimpleMovingAverage import SimpleMovingAverage
from BollingerBands import BollingerBands

from CandleStick_Indicator import CandleStick

from ExponentialMovingAverage import ExponentialMovingAverage
from RelativeStrengthIndex import RelativeStrengthIndex

class Algorithm:
    def __init__(self):
        self.sell_stock = False
        self.buy_stock = False
        self.do_nothing = False
        self.price = 0

        self.UpperBollingerBand = 0
        self.LowerBollingerBand = 0
        self.SimpleMovingAverage = 0
        self.stock_holdings = 0#change when live version
        self.holding_stock = False
        self.buyingpower = 500 #change later on to be based on api's net worth thing
        self.candlestick_body =[]
        self.candlestick_tail = []
        self.body_range = 0
        self.tail_range = 0
        self.tail_to_body = 0
        self.body_low = 0
        self.body_high = 0
        self.bought_price = 0
        self.price_high = 0
        self.sell_limit = 3
        self.counter =0
        self.first_MACD = 0
        self.prev_MACD = 0
        self.total_money_made = 0
        self.trades_completed = 0


        self.SMA_object = SimpleMovingAverage(self.price)
        self.BollingerBands_object = BollingerBands()


        self.CandleStickObject = CandleStick()
        self.Exponential_Moving_Average_Object = ExponentialMovingAverage()
        self.RelativeStrengthIndex_Object = RelativeStrengthIndex()

    def set_indicators(self, price, prev_12_prices, prev_26_prices, prev_53_prices, prev_20_values, count):
        self.price = price
        self.prev_12_prices = prev_12_prices
        self.prev_26_prices = prev_26_prices
        self.prev_53_prices = prev_53_prices
        self.twelve_EMA = self.Exponential_Moving_Average_Object.twelve_period_ema(self.price, self.prev_12_prices)
        self.twentysix_EMA = self.Exponential_Moving_Average_Object.twentysix_period_ema(self.price,self.prev_26_prices)
        self.fiftythree_EMA = self.Exponential_Moving_Average_Object.fiftythree_period_ema(self.price, self.prev_53_prices)
        self.MACD = self.Exponential_Moving_Average_Object.MACD()
        if count <= 21:
            self.SMA = self.SMA_object.before_20_values(self.price)
        else:
            self.SMA = self.SMA_object.after_20_values(self.price)
        self.UpperBollingerBand = self.BollingerBands_object.Calc_Upper_Band(prev_20_values, self.SMA)
        self.LowerBollingerBand = self.BollingerBands_object.Calc_Lower_Band(prev_20_values, self.SMA)
        self.RelativeStrengthIndex_Object.main(price)
    def triple_EMA_crossover(self):
        if self.twelve_EMA >= self.twentysix_EMA and self.twentysix_EMA >= self.fiftythree_EMA and self.holding_stock == True:
            self.sell_stock = True
            self.holding_stock = False
            self.money_made=self.price-self.bought_price
            self.total_money_made+=self.money_made
            self.trades_completed+=1
            return(self.total_money_made,self.trades_completed)
        elif self.twelve_EMA <= self.twentysix_EMA and self.twentysix_EMA <= self.fiftythree_EMA and self.holding_stock == False:
            self.buy_stock = True
            self.holding_stock = True
            self.bought_price=self.price
            return (self.total_money_made,self.trades_completed)
        else:
            self.do_nothing = True
            return (self.total_money_made,self.trades_completed)

    '''
    def triple_EMA_crossover(self):
        if self.twelve_EMA >= self.twentysix_EMA and self.twentysix_EMA >= self.fiftythree_EMA and self.holding_stock == True:
            self.sell_stock = True
            self.holding_stock = False
        elif self.twelve_EMA <= self.twentysix_EMA and self.twentysix_EMA <= self.fiftythree_EMA and self.holding_stock == False:
            self.buy_stock = True
            self.holding_stock = True
        else:
            self.do_nothing = True
    '''
    def moving_average_crossovers(self):
        if self.twelve_EMA >= self.twentysix_EMA and not self.holding_stock or self.twelve_EMA >= self.fiftythree_EMA and not self.holding_stock:
            self.buy_stock = True
            self.holding_stock = True
        elif self.twelve_EMA <= self.twentysix_EMA and self.holding_stock or self.twelve_EMA <= self.fiftythree_EMA and self.holding_stock:
            self.sell_stock = True
            self.holding_stock = False
        else:
            self.do_nothing = True

    def return_sell_state(self):
        return self.sell_stock
    def return_buy_state(self):
        return self.buy_stock
    def return_do_nothing(self):
        return self.do_nothing
    def return_holding_stock(self):
        return self.holding_stock
    def reset(self):
        self.sell_stock = False
        self.buy_stock = False
        self.do_nothing = False


'''
    def choose_action1(self, price, UpperBollingerBand, LowerBollingerBand):
        self.UpperBollingerBand = UpperBollingerBand
        self.LowerBollingerBand = LowerBollingerBand
        self.price = price
        self.sell_stock = False
        self.buy_stock = False
        self.do_nothing = False

        #Algorithm actual here
        if self.price > self.UpperBollingerBand and self.holding_stock == True:
            self.sell_stock = True
            self.holding_stock = False
            return self.sell_stock
        elif self.price < self.LowerBollingerBand and self.holding_stock == False:
            self.buy_stock = True
            self.holding_stock = True
            return self.buy_stock
        else:
            self.do_nothing = True
            return self.do_nothing
    def choose_action2(self, price, candlestick_body, candlestick_tail):
        self.price = price
        self.candlestick_body = candlestick_body
        self.candlestick_tail = candlestick_tail
        self.body_range = abs(self.candlestick_body[0] - self.candlestick_body[1])
        self.tail_range = abs(self.candlestick_tail[0] - self.candlestick_tail[1])
        self.buy_stock = False
        self.do_nothing = False
        self.sell_stock = False
        if self.candlestick_body[0] < self.candlestick_body[1]:  #checking if open is more or less than close and then defining as such
            self.body_low = self.candlestick_body[0]
            self.body_high = self.candlestick_body[1]
        else:

            self.body_low = self.candlestick_body[1]
            self.body_high = self.candlestick_body[0]
        if (self.candlestick_tail[0] - self.body_high)/4.5 >=self.body_range and self.holding_stock == True:
            self.sell_stock = True
            self.holding_stock = False
        elif abs(self.candlestick_tail[1] - self.body_low)/4.5 <= self.body_range and self.holding_stock == False:
            self.buy_stock = True
            self.holding_stock = True
        else:
            self.do_nothing = True
    def choose_action3(self, price, candlestick_body, candlestick_tail, UpperBollingerBand, LowerBollingerBand):
        self.price = price
        self.candlestick_body = candlestick_body
        self.candlestick_tail = candlestick_tail
        self.body_range = abs(self.candlestick_body[0] - self.candlestick_body[1])
        self.tail_range = abs(self.candlestick_tail[0] - self.candlestick_tail[1])
        self.UpperBollingerBand = UpperBollingerBand
        self.LowerBollingerBand = LowerBollingerBand
        self.buy_stock = False
        self.do_nothing = False
        self.sell_stock = False
        if self.candlestick_body[0] < self.candlestick_body[1]:
            self.body_low = self.candlestick_body[0]
            self.body_high = self.candlestick_body[1]
        else:
            self.body_low = self.candlestick_body[1]
            self.body_high = self.candlestick_body[0]
        if (self.candlestick_tail[0] - self.body_high) / 2 >= self.body_range and self.holding_stock == True and self.price > self.UpperBollingerBand:
            self.sell_stock = True
            self.holding_stock = False
        elif abs(self.candlestick_tail[1] - self.body_low) / 2 <= self.body_range and self.holding_stock == False and self.price < self.LowerBollingerBand:
            self.buy_stock = True
            self.holding_stock = True
        else:
            self.do_nothing = True
    def choose_action4(self, MACD, price): #diff from 5 cause it buys when dips below and sells when goes above, but for some reason makes money
        self.counter += 1
        self.MACD = MACD
        self.buy_stock = False
        self.do_nothing = False
        self.sell_stock = False
        self.prev_MACD = 0
        self.passed_MACD = 0

        if self.MACD == None:
            pass
        else:




            if self.MACD <=0 and self.MACD >=-0.02 and not self.holding_stock:
                self.buy_stock = True
                self.holding_stock = True

            elif self.MACD>= 0 and self.MACD <= 0.02 and self.holding_stock:
                self.sell_stock = True
                self.holding_stock = False
            else:
                self.do_nothing = True
    def choose_action5(self, MACD):
        self.MACD = MACD
        self.buy_stock = False
        self.do_nothing = False
        self.sell_stock = False

        self.passed_MACD = 0

        if self.MACD == None:
            pass
        else:

            # determining whether or not to buy based on the previous MACD
            if self.MACD >= 0 and self.MACD <= 0.02 and not self.holding_stock:
                self.buy_stock = True
                self.holding_stock = True

            elif self.MACD >= 0 and self.MACD <= 0.02 and self.holding_stock:
                self.sell_stock = True
                self.holding_stock = False
            else:
                self.do_nothing = True
        self.prev_MACD = self.MACD

    def choose_action6(self, MACD, candlestick_body, candlestick_tail):
        self.MACD = MACD

        self.prev_MACD = 0

        self.candlestick_body = candlestick_body
        self.candlestick_tail = candlestick_tail
        self.body_range = abs(self.candlestick_body[0] - self.candlestick_body[1])
        self.tail_range = abs(self.candlestick_tail[0] - self.candlestick_tail[1])
        if self.candlestick_body[0] < self.candlestick_body[1]:
            self.body_low = self.candlestick_body[0]
            self.body_high = self.candlestick_body[1]
        else:
            self.body_low = self.candlestick_body[1]
            self.body_high = self.candlestick_body[0]

        if self.MACD == None:
            self.do_nothing = True
        else:


            if self.MACD <=0 and self.MACD >=-0.02 and not self.holding_stock and abs(self.candlestick_tail[0] - self.body_high)/3 >=self.body_range:
                self.buy_stock = True
                self.holding_stock = True

            elif self.MACD>= 0 and self.MACD <= 0.02 and self.holding_stock and abs(self.candlestick_tail[1] - self.body_low)/3 <= self.body_range:
                self.sell_stock = True
                self.holding_stock = False
            else:
                self.do_nothing = True
    def choose_action7(self, twelve_EMA, twentysix_EMA):
        pass
'''





