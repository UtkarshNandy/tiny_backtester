import yfinance as yf
import pandas as pd

data = yf.download(
  ["AAPL", "MSFT", "SPY"],
  "2021-01-01",
  "2025-01-01",
  interval="1d",
  group_by="ticker",
  auto_adjust="True"
)

data.drop_duplicates()

# we will choose simple returns for P&L
aapl_sample = data["AAPL"]["Close"]
aapl_daily_returns = aapl_sample.pct_change()

# verify compounding math works

# manually compound calculation
initial_val = 100
compound_val = initial_val * (1 + aapl_daily_returns).prod()
manual_return = (compound_val - initial_val) / initial_val
print("Manual compounded return: " , manual_return)

# point to point calculation
point_to_point = (aapl_sample.iloc[-1] / aapl_sample.iloc[0]) - 1
print("Point-to-point return:", point_to_point)