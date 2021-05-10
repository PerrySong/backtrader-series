import datetime
import backtrader as bt
import pandas as pd

class MyStrategy(bt.Strategy):
    def __init__(self):
        print('init')

    def start(self):
        print('start')

    def prenext(self):
        print('prenext')

    def nextstart(self):
        print('next start')

    def next(self):
        print('next')
        # current close price
        print(self.date.close[0])

    def stop(self):
        print('stop')

# 1. Create a cerebro
cerebro = bt.Cerebro()

# 2. Add data feed
# 2.1 Create a data feed

df = pd.read_csv('../data/TSLA.csv')
# print(df.tail())
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)


tesla_daily = bt.feeds.PandasData(dataname=df, fromdate=datetime.datetime(2020, 5, 9), todate=datetime.datetime(2021, 5, 9))

# 2. Add the Data Feed to Cerebro
cerebro.adddata(tesla_daily)

# 3. Add strategy
cerebro.addstrategy(MyStrategy)

# 4. Run
cerebro.run()

# 5. plot
# cerebro.plot()
cerebro.plot(style='candle')