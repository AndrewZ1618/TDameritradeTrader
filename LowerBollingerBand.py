import math
class LowerBand:
    def __init__(self, prev_20_values, sma):
        self.prev_20_values = prev_20_values
        self.SMA = sma

        self.standard_dev = 0
        self.temp_standard_dev = 0
        self.price = 0
    def Calc_Lower_Band(self, prev_20_values, SMA):
        for i in range(len(self.prev_20_values)):
            self.temp_standard_dev = 0
            self.price = prev_20_values[i]
            self.temp_standard_dev = (self.price - self.SMA)**2

            self.standard_dev = self.standard_dev + self.temp_standard_dev

        self.standard_dev = self.standard_dev/10
        self.standard_dev = math.sqrt(abs(self.standard_dev))*2
        LowerBollingerBand = self.SMA - self.standard_dev
        return LowerBollingerBand