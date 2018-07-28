
"""
100DaysofMLCode

Day 2: July 27 2018

Starting towards building a quant model to predict capital markets.

"""

# Importing class object/libraries


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import quandl

# Generating random numbers from a normal distribution

X = np.random.normal(0,1,100)
X2 = np.random.normal(0,1,100)

# Plotting using matplotlib

plt.plot(X)
plt.plot(X2)
plt.xlabel('Time')
plt.ylabel('Returns')
plt.legend(['X','X2'])

plt.show()


# Importing Microsoft data from Quandl

quandl.ApiConfig.api_key = '6pS45JrDvUVDrvN9As7o'
data = quandl.get("EOD/MSFT", start_date = "2012-1-1", end_date = "2015-6-1")

X = data.Adj_Close

# Plotting adjusted closing price

plt.plot(X)
plt.show()

R = X.pct_change()[1:]

"""
100DaysofMLCode

Day 3: July 28 2018

Starting towards building a quant model to predict capital markets.

"""

# Plotting Microsoft returns via a histogram

plt.hist(R)
plt.xlabel("Returns")
plt.ylabel("Frequency")
plt.show()

# Plotting normally distributed data

plt.hist(np.random.normal(np.mean(R),np.std(R),10000), bins = 20)
plt.xlabel("Normal distributed returns")
plt.ylabel("Frequency")
plt.show()

# Calculate 30,60,90 day moving averages

MAVG = X.rolling(window = 30).mean()
MAVG2 = X.rolling(window = 60).mean()
MAVG3 = X.rolling( window = 90).mean()

# Plotting moving averages

plt.plot(X.index,X.values)
plt.plot(MAVG.index,MAVG.values)
plt.plot(MAVG2.index,MAVG2.values)
plt.plot(MAVG3.index,MAVG3.values)


plt.ylabel("MSFT price")
plt.legend(["MSFT","60 day MAVG"])
plt.show()







