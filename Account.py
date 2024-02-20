import requests
class Account:
    def __init__(self):
        self.endpoint = r"https://api.tdameritrade.com/v1/accounts"

        self.access_token = ''
        self.status_code = 0
    def get_account_data(self, access_token):
        self.access_token = access_token
        self.headers = {'Authorization':'Bearer {}'.format(access_token),
                        'Content-Type':'application/json'}

        while self.status_code != 200 and self.status_code != 201:

            self.response = requests.get(url=self.endpoint,headers=self.headers)

            self.status_code = self.response.status_code

        self.data = self.response.json()

        #print(self.data)

        self.account_balance = self.data[0]['securitiesAccount']['initialBalances']['accountValue']
        print(self.account_balance)

