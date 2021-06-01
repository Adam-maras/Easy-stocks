import requests

def get_ticker(name):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(name)
    result = requests.get(url).json()
    print(url)

    for x in result['ResultSet']['Result']:
        return x['symbol']

def ticker_to_name(ticker):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)
    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        return x['name']

def get_exchange(company_name):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(company_name)
    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        return x['exchDisp']
