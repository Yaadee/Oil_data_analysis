
import yfinance as yf
import pandas as pd
from datetime import datetime
# Define the ticker symbol for Brent Crude Oil
ticker = "BZ=F"

# Get data from Yahoo Finance
brent_data = yf.download(ticker, start="1987-5-20", end=datetime.now())

# Save to CSV
brent_data.to_csv('Inputs/data/raw_data/brent_oil_prices.csv')
