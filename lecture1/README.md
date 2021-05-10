# backtrader-series
Learning repo for backtrader

# Backtrader framework components

1. Cerebro : brain
2. Strategies 
3. Data Feeds
4. Ovservers
5. Writters
6. Analyzers

# Backtrader Workflow
1. Creating a cerebro
* cerebro = bt.Cerebro(**kwargs)
2. Add Data feeds
* data = bt.BacktraderCSVData(dataname='mypath.days', timeframe=bt.TimeFrame.days)
cerebro.adddata(data)
3. Add Strategies
cerebro.addstrategy(MyStrategy, myparam1=value1, myparam2=value2)
4. Other elements
* addwritter
* addanalyzer
* addobserver (or addobservermulti)
5. Changing the broker
* broker = MyBroker()
* cerebro.broker = broker
6. Run the strategy
* cerebro.run()
7. Plot
* cerebro.plot()

# Backtrader strategy
Life cycle:
1. __init__()
2. birth: start
3. Childhood: prenext()
4. nextstart()
5. Adult: next()
6. Death: stop()