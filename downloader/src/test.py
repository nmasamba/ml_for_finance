import urllib2


def download(file_path, url):
    # This function will download data from a URL and save it to a local specified file
    # Example usage: (1) set up local_path = '~/myurldata.csv' (2) pass in a local
    # file path and a download URL to the function e.g. download(local_path, yf_url)
    web_request = urllib2.Request(url)

    try:
        page = urllib2.urlopen(web_request)
        content = page.read()

        with open(file_path, "wb") as output:
            output.write(bytearray(content))

    except urllib2.HTTPError, e:
        print e.fp.read()

download("yahoo_data.txt", "https://finance.yahoo.com/quote/%5EGSPC/history?period1=1488740015&period2=1520276015&interval=1d&filter=history&frequency=1d")