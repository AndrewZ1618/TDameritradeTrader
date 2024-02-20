import requests
from config import client_id


class Price:
    def __init__(self):
        self.price = 0
        self.access_token = ''
        self.status_code = 0
        self.response = {}
        self.prev_price = 0
        self.count=0
    def get_price(self, access_token, symbol):
        self.access_token = access_token
        self.payload = ({'apikey': client_id})
        self.headers = {'Authorization':'Bearer {}'.format(access_token),
                  'Content-Type':'application/json'}
        self.endpoint = 'https://api.tdameritrade.com/v1/marketdata/{}/quotes'.format(symbol)
        self.response = {}
        try:
            while self.status_code != 200 and self.status_code != 201 and self.count<3:
                self.count+=1
                self.response = requests.get(url=self.endpoint,headers=self.headers, params=self.payload)

                self.status_code = self.response.status_code



            self.data = self.response.json()

            self.price = self.data[symbol]['askPrice']
            print(self.price)
        except KeyError:
            self.price = self.prev_price
            self.status_code = 0
            return self.prev_price


        self.status_code = 0
        self.prev_price = self.price
        self.count=0
        return self.price
def get_price_history(**kwargs):

    url = ('https://api.tdameritrade.com/v1/marketdata/{}/pricehistory').format(kwargs.get('symbol'))

    params = {}
    params.update({'apikey': client_id})

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)
    return requests.get(url, params=params).json()

#print(get_price_history(symbol='NVDA', period=1, periodType='day', frequencyType='minute'))