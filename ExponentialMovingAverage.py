import math

class ExponentialMovingAverage:
    def __init__(self):
        self.price = 0
        self.prev_12_EMA = 0
        self.prev_26_EMA = 0
        self.prev_53_EMA = 0
        self.prev_12_prices = []
        self.twelve_EMA = 0
        self.twentysix_EMA = 0
        self.SMA = 0
    def twelve_period_ema(self, price, prev_12_prices):

        self.price = price
        self.prev_12_prices = prev_12_prices
        if len(prev_12_prices) == 12:

            if self.prev_12_EMA == 0: #if first one and no prev ema
                for item in self.prev_12_prices:
                    self.SMA += item
                self.SMA = self.SMA / len(prev_12_prices)
                self.prev_12_EMA = self.SMA
                self.twelve_EMA = (price * (2 / 13)) + self.prev_12_EMA * (1 - 2 / 13)
                self.prev_12_EMA = self.twelve_EMA

                return self.twelve_EMA
            else:
                self.twelve_EMA = (price*(2/13)) + self.prev_12_EMA*(1-2/13)

                self.prev_12_EMA = self.twelve_EMA
                return self.twelve_EMA
        else:
            pass

    def twentysix_period_ema(self, price, prev_26_prices):

        self.price = price
        self.prev_26_prices = prev_26_prices
        self.SMA = 0
        if len(self.prev_26_prices) == 26:

            if self.prev_26_EMA == 0: #if first one and no prev ema

                for item in self.prev_26_prices:
                    self.SMA = self.SMA+  item
                self.SMA = self.SMA / len(prev_26_prices)
                self.prev_26_EMA = self.SMA
                self.twentysix_EMA = (price * (2 / 27)) + self.prev_26_EMA * (1 - 2 / 27)
                self.prev_26_EMA = self.twentysix_EMA

                return self.twentysix_EMA

            else:

                self.twentysix_EMA = (price*(2/27)) + self.prev_26_EMA*(1-2/27)

                self.prev_26_EMA = self.twentysix_EMA
                return self.twentysix_EMA

        else:
            pass
    def fiftythree_period_ema(self, price, prev_53_prices):

        self.price = price
        self.prev_53_prices = prev_53_prices
        self.SMA = 0
        if len(self.prev_53_prices) == 53:

            if self.prev_53_EMA == 0: #if first one and no prev ema

                for item in self.prev_53_prices:
                    self.SMA = self.SMA +  item
                self.SMA = self.SMA / len(prev_53_prices)
                self.prev_53_EMA = self.SMA
                self.fiftythree_EMA = (price * (2 / 54)) + self.prev_53_EMA * (1 - 2 / 54)
                self.prev_53_EMA = self.fiftythree_EMA

                return self.fiftythree_EMA

            else:

                self.fiftythree_EMA = (price*(2/54)) + self.prev_53_EMA*(1-2/54)

                self.prev_53_EMA = self.fiftythree_EMA
                return self.fiftythree_EMA

        else:
            pass
    def calc_ema(self, price, prev_prices, time_length): #won't work cause the prev ema only refers to that one thing
        self.price = price
        self.prev_prices = prev_prices
        self.SMA = 0
        self.time_length = time_length
        self.prev_EMA = 0
        if len(self.prev_prices) == self.time_length:

            if self.prev_26_EMA == 0:  # if first one and no prev ema

                for item in self.prev_26_prices:
                    self.SMA = self.SMA + item
                self.SMA = self.SMA / len(prev_26_prices)
                self.prev_26_EMA = self.SMA
                self.twentysix_EMA = (price * (2 / 27)) + self.prev_26_EMA * (1 - 2 / 27)
                self.prev_26_EMA = self.twentysix_EMA

                return self.twentysix_EMA

            else:

                self.twentysix_EMA = (price * (2 / 27)) + self.prev_26_EMA * (1 - 2 / 27)

                self.prev_26_EMA = self.twentysix_EMA
                return self.twentysix_EMA

        else:
            pass
    def MACD(self):
        if len(self.prev_26_prices) == 26:
            return self.twelve_EMA - self.twentysix_EMA

        else:

            pass
