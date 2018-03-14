
import urllib2
import datetime



def constructYFURL(ticker, start_date, end_date, freq):
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
    # IMPORTANT: Yahoo Finance API has changed, making it more difficult to carry out direct downloads
    start_date = datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    ticker = ticker.replace("^", "%5E")
    frequency = freq # can be 1d, 1wk or 1mo
    interval = freq # can be 1d, 1wk or 1mo
    period1 = str(start_date) # format" YYYY-MM-DD
    period2 = str(end_date) # format" YYYY-MM-DD
    yf_url = "https://finance.yahoo.com/quote/"+ticker+"/history?period1="+start_date+"&period2="+end_date+"&interval="+freq+"&filter=history&frequency="+freq
    return yf_url



def download(file_path, url):
    # This function will download data from a URL and save it to a local specified file
    # Example usage: (1) set up local_path = 'data.txt' (2) pass in a local
    # file path and a download URL to the function e.g. download(local_path, yf_url)
    web_request = urllib2.Request(url)

    try:
        page = urllib2.urlopen(web_request)
        content = page.read()

        with open(file_path, "wb") as output:
            output.write(bytearray(content))

    except urllib2.HTTPError, e:
        print e.fp.read()


if __name__ == "__main__":
    local_path = "yahoo_data.txt"

    # TO DO: update the URL constructing function so that it can be used here
    download_url = "https://finance.yahoo.com/quote/NFLX/history?period1=1489521384&period2=1521057384&interval=1d&filter=history&frequency=1d"
    
    download(local_path, download_url)