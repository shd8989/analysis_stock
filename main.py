# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.relativedelta import relativedelta

from pandas_datareader import data as pdr
import yfinance as yf

import matplotlib.pyplot as plt

yf.pdr_override()

now = datetime.now()
before_one_year = now - relativedelta(years=1)
start_dt = before_one_year.strftime("%Y-%m-%d")

# �Ｚ����
sec = pdr.get_data_yahoo('005930.KS', start=start_dt)
sec_dpc = (sec['Close']-sec['Close'].shift(1)) / sec['Close'].shift(1) * 100 # �ϰ� ������
sec_dpc.iloc[0] = 0 # �ϰ� �������� ù��° ���� Nan���� 0���� �ʱ�ȭ
sec_dpc_cs = sec_dpc.cumsum() # �ϰ� �������� ������

# Microsoft
msft = pdr.get_data_yahoo('MSFT', start=start_dt)
msft_dpc = (msft['Close']-msft['Close'].shift(1)) / msft['Close'].shift(1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cs = msft_dpc.cumsum()

# Apple
aapl = pdr.get_data_yahoo('AAPL', start=start_dt)
aapl_dpc = (aapl['Close']-aapl['Close'].shift(1)) / aapl['Close'].shift(1) * 100
aapl_dpc.iloc[0] = 0
aapl_dpc_cs = aapl_dpc.cumsum()

# Google
googl = pdr.get_data_yahoo('GOOGL', start=start_dt)
googl_dpc = (googl['Close']-googl['Close'].shift(1)) / googl['Close'].shift(1) * 100
googl_dpc.iloc[0] = 0
googl_dpc_cs = googl_dpc.cumsum()

plt.plot(sec.index, sec_dpc_cs, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cs, 'r--', label='Microsoft')
plt.plot(aapl.index, aapl_dpc_cs, 'g-', label='Apple')
plt.plot(googl.index, googl_dpc_cs, 'y-', label='Google')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()