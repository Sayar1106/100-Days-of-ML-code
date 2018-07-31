"""
100DaysofMLCode

Day 5: July 30 2018

Beta hedging
"""

# Importing libraries

import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
import math
import fix_yahoo_finance as yf
import statsmodels.api as sm
from statsmodels import regression
from pandas_datareader import data

# Generating stock returns

start = '2014-01-01'
end = '2015-01-01'

yf.pdr_override()

asset = data.get_data_yahoo("TSLA", start, end)
benchmark = data.get_data_yahoo("SPY", start, end)

r_a = asset['Adj Close'].pct_change()[1:]
r_b = benchmark['Adj Close'].pct_change()[1:]

r_a.plot()
r_b.plot()
plt.ylabel("Daily Return")
plt.legend(["Asset","benchmark"])
plt.show()
