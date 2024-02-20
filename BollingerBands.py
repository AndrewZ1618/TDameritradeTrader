import math
class BollingerBands:
    def __init__(self):
        self.prev_20_values = []
        self.SMA = 0

        self.standard_dev = 0
        self.temp_standard_dev = 0
        self.price = 0
        self.mult_value = 0.5
    def Calc_Upper_Band(self, prev_20_values, SMA):
        self.prev_20_values = prev_20_values
        self.SMA = SMA
        for i in range(len(self.prev_20_values)):
            self.temp_standard_dev = 0
            self.price = prev_20_values[i]
            self.temp_standard_dev = (self.price - self.SMA)**2

            self.standard_dev = self.standard_dev + self.temp_standard_dev

        self.standard_dev = self.standard_dev/10
        self.standard_dev = math.sqrt(abs(self.standard_dev))*self.mult_value
        UpperBollingerBand = self.SMA + self.standard_dev
        return UpperBollingerBand
    def Calc_Lower_Band(self, prev_20_values, SMA):
        self.prev_20_values = prev_20_values
        self.SMA = SMA
        for i in range(len(self.prev_20_values)):
            self.temp_standard_dev = 0
            self.price = prev_20_values[i]
            self.temp_standard_dev = (self.price - self.SMA)**2

            self.standard_dev = self.standard_dev + self.temp_standard_dev

        self.standard_dev = self.standard_dev/10
        self.standard_dev = math.sqrt(abs(self.standard_dev))*self.mult_value
        LowerBollingerBand = self.SMA - self.standard_dev
        return LowerBollingerBand

