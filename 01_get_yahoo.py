
from yahoo_finance import Share
from pprint import pprint

AAPL = Share('AAPL')

print AAPL.get_price()

pprint(AAPL.get_historical('2014-04-25', '2014-04-29'))