# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.relativedelta import relativedelta

from pandas_datareader import data as pdr
import yfinance as yf

import matplotlib.pyplot as plt

yf.pdr_override()

now = datetime.now()
before_one_year = now - relativedelta(years=3)
start_dt = before_one_year.strftime("%Y-%m-%d")

kospi = pdr.get_data_yahoo('^KS11', start_dt)
dow = pdr.get_data_yahoo('^DJI', start_dt)

window = 252
peak_ko = kospi['Adj Close'].rolling(window, min_periods=1).max() # 최고점
drawdown_ko = kospi['Adj Close']/peak_ko - 1.0 # 최고점 대비 낙폭률
max_dd_ko = drawdown_ko.rolling(window, min_periods=1).min() # 1년기간 단위 최대 손실 낙폭

peak_dow = dow['Adj Close'].rolling(window, min_periods=1).max()
drawdown_dow = dow['Adj Close']/peak_dow - 1.0
max_dd_dow = drawdown_dow.rolling(window, min_periods=1).min()

plt.figure(figsize=(9, 7))
plt.subplot(221) # 2행2열 중 첫번째
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(222)
dow['Close'].plot(label='Dow Jones', title='Dow Jones MDD', grid=True, legend=True)

plt.subplot(223)
drawdown_ko.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd_ko.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.subplot(224)
drawdown_dow.plot(c='blue', label='Dow Jones DD', grid=True, legend=True)
max_dd_dow.plot(c='red', label='Dow Jones MDD', grid=True, legend=True)
plt.show()