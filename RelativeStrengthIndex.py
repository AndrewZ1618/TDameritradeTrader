class RelativeStrengthIndex:
    def __init__(self):
        self.price = 0.0
        self.last_14_price_list = []
        self.gains_list = []
        self.losses_list = []
        self.previous_price = 0.0
        self.average_gain = 0.0
        self.average_loss = 0.0
        self.rsi_value = 0.0
        self.relative_strength = 0.0
        self.current_gain=0.0
        self.current_loss=0.0
        self.previous_average_gain=0.0
        self.previous_average_loss=0.0
        self.count=0

    def main(self, price):
        self.price = price
        self.last_14_price_list.append(self.price)
        if self.count == 0:
            self.previous_price = self.price
            self.count = self.count + 1
        elif self.count < 14:
            self.first_14_prices()
            self.previous_price = self.price
            self.count = self.count + 1
        elif self.count == 14:
            self.only_14_prices()
            #self.previous_price = self.price
            self.previous_price = self.price
            self.previous_average_gain = self.average_gain
            self.previous_average_loss = self.average_loss
            self.count = self.count + 1
            return self.rsi_value
        else:
            self.after_14_prices()
            self.previous_price = self.price
            self.previous_average_gain=self.average_gain
            self.previous_average_loss = self.average_loss
            self.count = self.count + 1
            return self.rsi_value

    def first_14_prices(self):
        self.gains_or_losses()

    def only_14_prices(self):
        self.gains_or_losses()
        self.average_gains_and_losses()
        self.calculate_rsi()

    def after_14_prices(self):
        self.gains_or_losses()
        self.formula_gains_and_losses()
        self.calculate_rsi()

    def gains_or_losses(self):
        if self.previous_price < self.price:
            self.gains_list.append(self.price - self.previous_price)
            self.losses_list.append(0)
            self.current_gain=self.price - self.previous_price
            self.current_loss=0
        elif self.previous_price > self.price:
            self.losses_list.append(self.previous_price - self.price)
            self.gains_list.append(0)
            self.current_loss = self.previous_price-self.price
            self.current_gain = 0
        else:
            self.gains_list.append(0)
            self.losses_list.append(0)
            self.current_loss = 0
            self.current_gain = 0

    def average_gains_and_losses(self):
        self.average_gain = sum(self.gains_list) / len(self.gains_list)
        self.average_loss = sum(self.losses_list) / len(self.losses_list)

    def formula_gains_and_losses(self):
        self.average_gain=((self.previous_average_gain*13)+self.current_gain)/14
        self.average_loss=((self.previous_average_loss*13)+self.current_loss)/14

    def calculate_rsi(self):
        try:
            self.relative_strength = self.average_gain / self.average_loss
            self.rsi_value = 100 - (100 / (1 + self.relative_strength))
        except(ZeroDivisionError):
            self.rsi_value = 100.0



