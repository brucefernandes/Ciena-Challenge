# %%
import pandas as pd
import numpy as np

stock_prices_init = pd.read_csv('../stocks.csv')
stock_prices = stock_prices_init.copy()
stock_prices.set_index("Date", inplace=True, drop=True)

def highest_prices(years):
  #first we determine the yearly range asked for
  if years not in range(1,11):
    return "ERROR: Enter a valid number between 1 to 10"
  
  start_year = str(2023 - years)
  
  stock_prices_in_range = stock_prices.loc[start_year + '-1-1 00:00:00' : '2023-1-1 00:00:00']
  maximum_stock_prices = stock_prices_in_range.max()
  top_10_tickers = maximum_stock_prices.nlargest(10)

  return top_10_tickers



def most_volatile(years):
  #first we determine the yearly range asked for
  if years not in range(1,11):
    return "ERROR: Enter a valid number between 1 to 10"
  
  start_year = str(2023 - years)
  stock_prices_in_range = stock_prices.loc[start_year + '-1-1 00:00:00' : '2023-1-1 00:00:00']

  log_returns = np.log(stock_prices_in_range).diff() #calculate instantaneous returns 

  log_returns.dropna(how='all',axis=0, inplace=True) #removes first row sinces it has NaN
  
  standard_deviation = log_returns.std()
  volatility = standard_deviation * np.sqrt(252) * 100 

  # TRADING_DAYS = len(log_returns)
  # rolling_volatility = log_returns.rolling(window=TRADING_DAYS).std()*np.sqrt(TRADING_DAYS) * 100

  
  return volatility.nlargest(10)



# %%
def least_volatile(years):
  #first we determine the yearly range asked for
  if years not in range(1,11):
    return "ERROR: Enter a valid number between 1 to 10"
  
  start_year = str(2023 - years)
  stock_prices_in_range = stock_prices.loc[start_year + '-1-1 00:00:00' : '2023-1-1 00:00:00']

  log_returns = np.log(stock_prices_in_range).diff() #calculate instantaneous returns 

  log_returns.dropna(how='all',axis=0, inplace=True) #removes first row sinces it has NaN
  
  standard_deviation = log_returns.std()
  volatility = standard_deviation * np.sqrt(252) * 100 
  
  return volatility.nsmallest(10)

# %%
print('--------------------------------------------------------------------------------------------------------------')
print('Top 10 Highest Stocks in 1 year:-\n')
print(highest_prices(1))
print('--------------------------------------------------------------------------------------------------------------')
print("Top 10 most volatile stocks in 1 year\n")
print(most_volatile(10))
print('--------------------------------------------------------------------------------------------------------------')
print("Top 10 least volatile stocks in 1 year\n")
print(least_volatile(10))