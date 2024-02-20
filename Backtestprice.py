import csv
class csv_price:
    def __init__(self, file):
        self.file = file
        self.price = 0
        self.rows = []
        self.count = 0
    def get_csv_price(self):
        try:
            with open(self.file, 'r') as NVDA:
                reader = list(csv.reader(NVDA))

                self.count = self.count + 1
                row = (reader[self.count])

                self.price = row[0]
                self.price = float(self.price)
                return self.price
        except FileNotFoundError:
            print("File not found")
            print(self.file)
            return False
    def counter(self):
        return self.count




