
from yahoo_finance import Share
from pprint import pprint

AAPL = Share('AAPL')

print AAPL.get_price()

pprint(AAPL.get_historical('2014-04-25', '2014-04-29'))


# actual URL
https://finance.yahoo.com/quote/%5EGSPC/history?period1=1519257600&period2=1519689600&interval=1d&filter=history&frequency=1d