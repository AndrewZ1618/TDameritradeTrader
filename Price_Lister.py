class Price_Lister:
    def __init__(self):
        self.prev_12_prices = []
        self.prev_26_prices = []
        self.prev_20_prices = []
        self.prev_53_prices = []

    def prev_price_lister(self, price):
        if len(self.prev_12_prices) <= 11:
            self.prev_12_prices.append(price)
        else:
            self.prev_12_prices.append(price)
            self.prev_12_prices.pop(0)
        if len(self.prev_26_prices) <= 25:
            self.prev_26_prices.append(price)
        else:
            self.prev_26_prices.append(price)
            self.prev_26_prices.pop(0)
        if len(self.prev_26_prices) <= 25:
            self.prev_26_prices.append(price)
        else:
            self.prev_26_prices.append(price)
            self.prev_26_prices.pop(0)
        if len(self.prev_20_prices) <= 19:
            self.prev_20_prices.append(price)
        else:
            self.prev_20_prices.append(price)
            self.prev_20_prices.pop(0)
        if len(self.prev_53_prices) <= 52:
            self.prev_53_prices.append(price)
        else:
            self.prev_53_prices.append(price)
            self.prev_53_prices.pop(0)
    def return_prev_12_prices(self):
        return self.prev_12_prices
    def return_prev_26_prices(self):
        return self.prev_26_prices
    def return_prev_20_prices(self):
        return self.prev_20_prices
    def return_prev_53_prices(self):
        return  self.prev_53_prices