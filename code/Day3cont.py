"""
100DaysofMLCode

Day 3: July 28 2018

Starting towards building a quant model to predict capital markets.

"""

# Importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data
from datetime import datetime
import fix_yahoo_finance as yf

# Generating random numbers

X = np.random.randn(50)
Y = np.random.randn(50)

# Plotting random numbers

plt.scatter(X,Y)
plt.xlabel('X value')
plt.ylabel('Y value')
plt.show()

print ("Correlation " + str(np.cov(X,Y)[0,1]/(np.std(X)*np.std(Y))))
print ("Built-in correlation " + str(np.corrcoef(X,Y)[0,1]))

# Pull pricing data of two stocks in the S&P 500 market

"""
100DaysofMLCode

Day 4: July 29 2018

Starting towards building a quant model to predict capital markets.

"""

start = '2013-1-1'
end = '2015-1-1'

yf.pdr_override()

a1 = data.get_data_yahoo("LRCX",start, end)
a2 = data.get_data_yahoo('AAPL', start, end)

plt.scatter(a1['Adj Close'],a2['Adj Close'])
plt.xlabel("LRCX")
plt.ylabel("AAPL")
plt.title("Stock prices from " + start + " to " + end)
plt.show()


rolling_coef = pd.rolling_corr(a1['Adj Close'],a2['Adj Close'],60)

plt.plot(rolling_coef)
plt.xlabel('Day')
plt.ylabel('60 day Rolling correlation')
plt.show()

