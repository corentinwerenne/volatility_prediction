#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:08:22 2022

@author: Corentin Werenne
"""

import yfinance as yf
import pandas as pd

def get_sp500_ticker_list():
    """
    Returns a list with all SP500 tickers
    """
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    tables = pd.read_html(url)
    table = tables[0]
    ticker_list = table['Symbol']
    return ticker_list

def get_adj_close(ticker_list, start, end, interval):
    """
    Returns the adjusted close for a unique ticker as string or a list of tickers.
    Format of dates: 'yyyy-mm-dd'
    Possible intervals: '1d', '5d', '1mo' 
    or intraday measures but limited to max a week's worth: '1m', '2m', '5m', '15m', '30m'
    """
    full_df = yf.download(ticker_list, start=start, end=end, interval=interval)
    adj_close_df = full_df['Adj Close']
    return adj_close_df

def sp500_closes_to_csv(start, end, interval):
    """
    Saves adjusted closes for all  SP500 companies in a csv file
    Format of dates: 'yyyy-mm-dd'
    Possible intervals: '1d', '5d', '1mo' 
    or intraday measures but limited to max a week's worth: '1m', '2m', '5m', '15m', '30m'
    """
    ticker_list = get_sp500_ticker_list()
    adj_closes = get_adj_close(ticker_list, start, end, interval)
    adj_closes.to_csv('sp500_ajdclose.csv')
    