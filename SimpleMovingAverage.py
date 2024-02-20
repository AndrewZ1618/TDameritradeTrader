class SimpleMovingAverage:
    def __init__(self, price):

        self.prev_20_values = []
        self.price = price
        self.SMA = 0
    def before_20_values(self, price):
        self.prev_20_values.append(price)
        self.SMA = 0.0
        return self.SMA
        return self.prev_20_values
    def after_20_values(self, price):
        self.SMA = 0
        self.prev_20_values.append(price)
        del self.prev_20_values[0]
        for item in self.prev_20_values:
            self.SMA = self.SMA + item
        self.SMA  = self.SMA / 20
        return self.SMA
        return self.prev_20_values
    def return_prev_20_values(self):
        return self.prev_20_values
    def reset(self):
        self.prev_20_values = []
        self.price = price
        self.SMA = 0