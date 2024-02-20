import time
import urllib
import requests
#from splinter import Browser
from config import client_id, refresh_token
class AccessToken:
    def __init__(self):
        #define shit for later
        #self.executable_path={'executable_path': r'C:\Users\jzwei\OneDrive - The Athenian School\Documents\Athenian 2020-2021\Documents\PycharmProjects\chromedriver'}
        #self.browser=Browser('chrome',**self.executable_path,headless=False)
        self.client_code=client_id+'@AMER.OAUTHAP'
        self.status=0
        self.count = 0
    def main(self):
        #calls all other functions needed
        try:
            self.visit_url()
        except TimeoutError:
            pass
        return(self.access_token)
    def visit_url(self):
        self.url='https://api.tdameritrade.com/v1/oauth2/token'
        self.headers={'Content-Type':"application/x-www-form-urlencoded"}
        payload={'grant_type': 'refresh_token','refresh_token': refresh_token,'client_id': self.client_code}
        #print('test')
        while self.status != 200 and self.status != 201 and self.count<=3:
            self.count+=1
            authReply=requests.post(self.url,headers=self.headers,data=payload)
            self.status=authReply.status_code
            print(self.status)
            print(authReply.json())
        self.status=0
        self.count = 0

        decoded_content=authReply.json()
        self.access_token=decoded_content['access_token']

'''
import requests
import json
from config import client_id, refresh_token
class AccessToken:
    def __init__(self):
        self.access_token = ''
        self.params = {}
        self.url = 'https://api.tdameritrade.com/v1/oauth2/token'
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}
    def get_access_token(self):
        self.status = 0
        try:
            self.payload = {
                'grant_type':'refresh_token',
                'refresh_token': refresh_token,
                'client_id': client_id

            }
            while self.status != 200 and self.status !=201:
                response = requests.post(url=self.url,headers=self.headers,data=self.payload)

                response_json = response.json()
                self.access_token = response_json['access_token']
                self.status = response.status_code
        except KeyError:
            self.access_token = self.access_token

    def write_access_token(self):
        f = open('tokens/access_token.txt', 'w')
        f.write(self.access_token)
        f.close()
    def main(self):
        self.get_access_token()

        return self.access_token

'''
