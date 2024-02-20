import csv
from Backtestprice import csv_price
from SimpleMovingAverage import SimpleMovingAverage
from BollingerBands import BollingerBands
from Algorithm import Algorithm
from BuyOrSell import Action
from CandleStick_Indicator import CandleStick
from Price_Lister import Price_Lister
from ExponentialMovingAverage import ExponentialMovingAverage


def algorithm1():
    # objects
    price_getter = csv_price()
    price = price_getter.get_csv_price()
    SMA_object = SimpleMovingAverage(price)
    BollingerBands_object = BollingerBands()
    Algorithm_object = Algorithm(price)
    Action_object = Action(price)
    CandleStickObject = CandleStick()

    for i in range(2000):
        try:
            price = price_getter.get_csv_price()
            count = price_getter.counter()

            if count <= 21:
                SMA = SMA_object.before_20_values(price)


            else:
                SMA = SMA_object.after_20_values(price)
                prev_20_values = SMA_object.return_prev_20_values()
                UpperBollingerBand = BollingerBands_object.Calc_Upper_Band(prev_20_values, SMA)
                LowerBollingerBand = BollingerBands_object.Calc_Lower_Band(prev_20_values, SMA)

                Algorithm_object.choose_action1(UpperBollingerBand, LowerBollingerBand, price)
                sell_state = Algorithm_object.return_sell_state()
                buy_state = Algorithm_object.return_buy_state()
                wait_state = Algorithm_object.return_do_nothing()

                if wait_state:
                    pass
                elif sell_state:
                    Action_object.sell(price)

                elif buy_state == True:
                    Action_object.buy(price)

                else:
                    print("what the fuck ay yo man what the fuck what da faaaaaaaaaaaaaaack")

                Algorithm_object.reset()




        except IndexError:
            SMA_object.reset()
            profit = Action.return_profits()
            print(profit)
            break


def algorithm2():
    price_getter = csv_price()
    price = price_getter.get_csv_price()
    SMA_object = SimpleMovingAverage(price)
    BollingerBands_object = BollingerBands()
    Algorithm_object = Algorithm(price)
    Action_object = Action(price)
    CandleStickObject = CandleStick()

    for x in range(2000):
        try:
            price = price_getter.get_csv_price()
            count = price_getter.counter()
            prev_20_values = SMA_object.return_prev_20_values()

            if count <= 21:
                SMA = SMA_object.before_20_values(price)


            else:
                SMA = SMA_object.after_20_values(price)
                if x % 20 == 0:
                    CandleStickObject.calc_candlestick(price, prev_20_values)

                    candlestick_body = CandleStickObject.return_body()
                    candlestick_tail = CandleStickObject.return_tail()

                    Algorithm_object.choose_action2(price, candlestick_body, candlestick_tail)
                    sell_state = Algorithm_object.return_sell_state()
                    buy_state = Algorithm_object.return_buy_state()
                    wait_state = Algorithm_object.return_do_nothing()

                    if wait_state:
                        pass
                    elif sell_state:
                        Action_object.sell(price)

                    elif buy_state == True:
                        Action_object.buy(price)

                    else:
                        print("what the fuck ay yo man what the fuck what da faaaaaaaaaaaaaaack")

                    Algorithm_object.reset()
                else:

                    pass
                CandleStickObject.reset()
                prev_price = price




        except IndexError:
            price = prev_price
            break


def algorithm3():
    price_getter = csv_price()
    price = price_getter.get_csv_price()
    SMA_object = SimpleMovingAverage(price)
    BollingerBands_object = BollingerBands()
    Algorithm_object = Algorithm(price)
    Action_object = Action(price)
    CandleStickObject = CandleStick()
    for x in range(2000):
        try:
            price = price_getter.get_csv_price()
            count = price_getter.counter()
            prev_20_values = SMA_object.return_prev_20_values()
            Price_Lister_object.prev_price_lister(price)
            if count <= 21:
                SMA = SMA_object.before_20_values(price)


            else:
                SMA = SMA_object.after_20_values(price)
                if x % 20 == 0:
                    CandleStickObject.calc_candlestick(price, prev_20_values)

                    candlestick_body = CandleStickObject.return_body()
                    candlestick_tail = CandleStickObject.return_tail()
                    SMA = SMA_object.after_20_values(price)
                    prev_20_values = SMA_object.return_prev_20_values()
                    UpperBollingerBand = BollingerBands_object.Calc_Upper_Band(prev_20_values, SMA)
                    LowerBollingerBand = BollingerBands_object.Calc_Lower_Band(prev_20_values, SMA)
                    Algorithm_object.choose_action3(price, candlestick_body, candlestick_tail, UpperBollingerBand,
                                                    LowerBollingerBand)
                    sell_state = Algorithm_object.return_sell_state()
                    buy_state = Algorithm_object.return_buy_state()
                    wait_state = Algorithm_object.return_do_nothing()

                    if wait_state:
                        pass
                    elif sell_state:
                        Action_object.sell(price)

                    elif buy_state == True:
                        Action_object.buy(price)

                    else:
                        print("what the fuck ay yo man what the fuck what da faaaaaaaaaaaaaaack")

                    Algorithm_object.reset()
                else:

                    pass
                CandleStickObject.reset()
                prev_price = price




        except IndexError:
            price = prev_price
            break


def algorithm4():
    price_getter = csv_price()
    price = price_getter.get_csv_price()
    SMA_object = SimpleMovingAverage(price)
    BollingerBands_object = BollingerBands()
    Algorithm_object = Algorithm(price)
    Action_object = Action(price)
    CandleStickObject = CandleStick()
    Price_Lister_object = Price_Lister()
    Exponential_Moving_Average_Object = ExponentialMovingAverage()
    while True:
        try:
            price = price_getter.get_csv_price()
            count = price_getter.counter()
            prev_20_values = SMA_object.return_prev_20_values()
            Price_Lister_object.prev_price_lister(price)

            if count >= 27:

                SMA = SMA_object.after_20_values(price)

                prev_12_prices = Price_Lister_object.return_prev_12_prices()
                prev_26_prices = Price_Lister_object.return_prev_26_prices()
                twelve_EMA = Exponential_Moving_Average_Object.twelve_period_ema(price, prev_12_prices)
                twentysix_EMA = Exponential_Moving_Average_Object.twentysix_period_ema(price, prev_26_prices)
                MACD = Exponential_Moving_Average_Object.MACD()
                Algorithm_object.choose_action4(MACD, price)

                sell_state = Algorithm_object.return_sell_state()
                buy_state = Algorithm_object.return_buy_state()
                wait_state = Algorithm_object.return_do_nothing()

                if wait_state:
                    pass
                elif sell_state:
                    Action_object.sell(price)

                elif buy_state == True:
                    Action_object.buy(price)

                else:
                    print("what the fuck ay yo man what the fuck what da faaaaaaaaaaaaaaack")

                Algorithm_object.reset()
            else:
                pass



        except IndexError:
            break


def algorithm5():
    price_getter = csv_price()
    price = price_getter.get_csv_price()
    SMA_object = SimpleMovingAverage(price)
    BollingerBands_object = BollingerBands()
    Algorithm_object = Algorithm(price)
    Action_object = Action(price)
    CandleStickObject = CandleStick()
    Price_Lister_object = Price_Lister()
    Exponential_Moving_Average_Object = ExponentialMovingAverage()
    while True:
        try:
            price = price_getter.get_csv_price()
            count = price_getter.counter()
            prev_20_values = SMA_object.return_prev_20_values()
            Price_Lister_object.prev_price_lister(price)

            if count >= 27:

                SMA = SMA_object.after_20_values(price)

                prev_12_prices = Price_Lister_object.return_prev_12_prices()
                prev_26_prices = Price_Lister_object.return_prev_26_prices()
                twelve_EMA = Exponential_Moving_Average_Object.twelve_period_ema(price, prev_12_prices)
                twentysix_EMA = Exponential_Moving_Average_Object.twentysix_period_ema(price, prev_26_prices)
                MACD = Exponential_Moving_Average_Object.MACD()
                Algorithm_object.choose_action5(MACD)

                sell_state = Algorithm_object.return_sell_state()
                buy_state = Algorithm_object.return_buy_state()
                wait_state = Algorithm_object.return_do_nothing()

                if wait_state:
                    pass
                elif sell_state:
                    Action_object.sell(price)

                elif buy_state == True:
                    Action_object.buy(price)

                else:
                    print("what the fuck ay yo man what the fuck what da faaaaaaaaaaaaaaack")

                Algorithm_object.reset()
            else:
                pass



        except IndexError:
            break


def algorithm6():
    price_getter = csv_price()
    price = price_getter.get_csv_price()
    SMA_object = SimpleMovingAverage(price)
    BollingerBands_object = BollingerBands()
    Algorithm_object = Algorithm(price)
    Action_object = Action(price)
    CandleStickObject = CandleStick()
    Price_Lister_object = Price_Lister()
    Exponential_Moving_Average_Object = ExponentialMovingAverage()
    while True:
        try:
            price = price_getter.get_csv_price()
            count = price_getter.counter()
            prev_20_values = SMA_object.return_prev_20_values()
            Price_Lister_object.prev_price_lister(price)

            if count <= 21:
                SMA = SMA_object.before_20_values(price)


            else:
                SMA = SMA_object.after_20_values(price)

            if count >= 27:

                SMA = SMA_object.after_20_values(price)

                prev_12_prices = Price_Lister_object.return_prev_12_prices()
                prev_26_prices = Price_Lister_object.return_prev_26_prices()
                twelve_EMA = Exponential_Moving_Average_Object.twelve_period_ema(price, prev_12_prices)
                twentysix_EMA = Exponential_Moving_Average_Object.twentysix_period_ema(price, prev_26_prices)
                MACD = Exponential_Moving_Average_Object.MACD()

                CandleStickObject.calc_candlestick(price, prev_20_values)

                candlestick_body = CandleStickObject.return_body()
                candlestick_tail = CandleStickObject.return_tail()
                Algorithm_object.choose_action6(MACD, candlestick_body, candlestick_tail)

                sell_state = Algorithm_object.return_sell_state()
                buy_state = Algorithm_object.return_buy_state()
                wait_state = Algorithm_object.return_do_nothing()

                if wait_state:
                    pass
                elif sell_state:
                    Action_object.sell(price)

                elif buy_state == True:
                    Action_object.buy(price)

                else:
                    print("fuck")

                Algorithm_object.reset()
            else:
                pass



        except IndexError:
            break


if __name__ == '__main__':
    # algorithm1()
    # algorithm2()
    # algorithm3()
    # algorithm4()
    algorithm5()
    # algorithm6()