import pandas as pd
import yfinance as yf
from yfinance.exceptions import YFinanceException
from requests import HTTPError, ConnectionError
from time import sleep

def sector(ticker_symbol):
    try:
        return yf.Ticker(ticker_symbol).info["sector"]
    except KeyError:
        print(yf.Ticker(ticker_symbol).info)
        return "Not Found"
    except (HTTPError, ConnectionError, YFinanceException) as e:
        print(e)
        return "Not Found"


if __name__ == "__main__":
    stocks = pd.read_excel("../trading_data/congress-trading-all.xlsx")
    symbol2sector = dict()
    for ticker_symbol in stocks.Ticker.unique():
        symbol2sector[ticker_symbol] = sector(ticker_symbol)
        print(ticker_symbol, symbol2sector[ticker_symbol])
        sleep(0.5)
    symbol2sectordf = pd.DataFrame(symbol2sector).transpose()
    symbol2sectordf.to_csv("../trading_data/symbol2sector.csv")

