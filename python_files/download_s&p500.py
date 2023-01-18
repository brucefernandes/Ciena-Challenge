# %%
import pandas as pd
import yfinance as yf

# %% [markdown]
# 1.  Scrape the S&P500 wiki using pandas "read_html" function to grab the list of tickers/symbols. 

# %%
sp_wiki = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp_wiki_df = pd.read_html(sp_wiki)

# %% [markdown]
# 2. Grab symbol values from the first table and force it into a list. 

# %%
sp_tickers = list(sp_wiki_df[0]['Symbol'].values) #grab the first table & grab the symbol values and force it into a list

# %% [markdown]
# 3. Feed the yahoo finance download function the ticker list and the following parameters (start date, end date and interval)

# %%
data = yf.download(sp_tickers, start="2012-12-31", end="2023-01-01", interval ="1d")

# %% [markdown]
# 4. Grab the Adjusted Close column. This column expresses the closing price of stock which referes to the price of a stock after divindends are paid off

# %%
stock_prices = data['Adj Close']

# %%
stock_prices.to_csv('../stocks.csv', index=True)

print('Done')
