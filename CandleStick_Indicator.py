class CandleStick:
    def __init__(self):
        self.price = 0
        self.prev_20_values = []
        self.body = [] #first number is open, second is close
        self.tail = [] #first number is high, second is low
        self.high = 0
        self.low = 1001000000000000
        self.open = 0
        self.close = 0
    def calc_candlestick(self, price, prev_20_values):
        self.prev_20_values = prev_20_values
        for item in self.prev_20_values:
            if item > self.high:
                self.high = item
            elif item < self.low:
                self.low = item
        self.tail.append(self.high)
        self.tail.append(self.low)
        self.open = self.prev_20_values[0]
        self.close = self.prev_20_values[19]
        self.body.append(self.open)
        self.body.append(self.close)

    def return_body(self):
        return self.body
    def return_tail(self):
        return self.tail
    def reset(self):


        self.price = 0
        self.prev_20_values = []
        self.body = [] #first number is open, second is close
        self.tail = [] #first number is high, second is low
        self.high = 0
        self.low = 1000000000000000
        self.open = 0
        self.close = 0

