
# Code to download data for a given ticker
# Parameters: ticker, start date, end date, frequency



# S&P 500 Daily - 2 Mar 2017 - 2 Mar 2018
# https://finance.yahoo.com/quote/%5EGSPC/history?period1=1488487184&period2=1520023184&interval=1d&filter=history&frequency=1d
# AAPL Daily
# https://finance.yahoo.com/quote/AAPL/history?period1=1488487184&period2=1520023184&interval=1d&filter=history&frequency=1d

# S&P 500 Weekly - 2 Mar 2017 - 2 Mar 2018
# https://finance.yahoo.com/quote/%5EGSPC/history?period1=1488486755&period2=1520022755&interval=1wk&filter=history&frequency=1wk


# S&P 500 Monthly - 2 Mar 2017 - 2 Mar 2018
# https://finance.yahoo.com/quote/%5EGSPC/history?period1=1488486755&period2=1520022755&interval=1mo&filter=history&frequency=1mo

def constructYFURL(ticker, start_date, end_date, freq):
    start_date = datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    # Yahoo Finance API has changed, making it more difficult to carry out direct downloads
    ticker = ticker.replace("^", "%5E")
    frequency = freq # can be 1d, 1wk or 1mo
    interval = freq # can be 1d, 1wk or 1mo
    period1 = str(start_date) # format" YYYY-MM-DD
    period2 = str(end_date) # format" YYYY-MM-DD
    yf_url = "https://finance.yahoo.com/quote/"+ticker+"/history?period1="+start_date+"&period2="+end_date"&interval="+freq"&filter=history&frequency="+freq
    return yf_url
