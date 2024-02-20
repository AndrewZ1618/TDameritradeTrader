import bs4 as bs
import lxml
import datetime
from datetime import datetime
from datetime import date
import time

import requests
import csv


def get_price():
    retry = True
    while retry == True:
        try:
            resp = requests.get("https://finance.yahoo.com/quote/NVDA?p=NVDA")
            soup = bs.BeautifulSoup(resp.text, "lxml")
            price = soup.find('span', class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text.strip()
            price = price.replace(',', '')
        except (IndexError, AttributeError, TypeError):
            pass
        else:
            print(price)
            retry = False
    return price


def write_csv():
    price=get_price()
    with open("databases/backtest_data{}.csv".format(date.today()), 'a', newline='') as backtest_data:
        csv_writer = csv.writer(backtest_data, delimiter=',')
        csv_writer.writerow([price])


def timer():

    while True:
        now = datetime.now()
        sixAM = now.replace(hour=6, minute=30)
        onePM = now.replace(hour=13, minute=0)
        if now > sixAM and now < onePM:
            write_csv()
            time.sleep(5)
        else:
            now = datetime.now()
            print(now)
            time.sleep(60)

timer()