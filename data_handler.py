#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:08:22 2022

@author: corentin
"""

import yfinance as yf

def get_adj_close(ticker_list, start, end, interval):
    full_df = yf.download(ticker_list, start=start, end=end, interval=interval)
    adj_close_df = full_df['Adj Close']
    return adj_close_df

# start='2018-01-01'
# end='2020-12-31'
# interval='1mo'
# ticker_list = ['AAPL', 'NVDA', 'FTNT']

# df = get_data(ticker_list, start, end, interval)


