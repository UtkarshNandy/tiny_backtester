import yfinance as yf
import pandas as pd
import os
import pickle
import matplotlib.pyplot as plt
from strategy import run_momentum_strategy

data_file = "../data/data.pkl"

if os.path.exists(data_file):
  try:
    with open(data_file, "rb") as f:
      data = pickle.load(f)
  except (EOFError, pickle.UnpicklingError):
    print("Corrupted data file. Download fresh data..")
    os.remove(data_file)
else:
  data = yf.download(
  ["AAPL", "MSFT", "SPY"],
  "2005-01-01",
  "2025-01-01",
  interval="1d",
  group_by="ticker",
  auto_adjust="True"
  )
  with open (data_file, "wb") as f:
    pickle.dump(data , f)
  
  
pd.set_option("display.max_rows", None) 
data.drop_duplicates()

# we will choose simple returns for P&L
aapl_prices = data["AAPL"]["Close"]
aapl_daily_returns = aapl_prices.pct_change().fillna(0)

# verify compounding math works
# manually compound calculation
initial_val = 100
compound_val = initial_val * (1 + aapl_daily_returns).prod()
manual_return = (compound_val - initial_val) / initial_val
print("Manual compounded return: " , manual_return)

# loop through each ticker and perform strategy
TCKRS = ["AAPL", "SPY" , "MSFT"]
all_results = {}
all_equity_curves = {}

for ticker in TCKRS:
  prices = data[ticker]["Close"]
  equity_curve, results = run_momentum_strategy(prices)

  all_results[ticker] = results
  all_equity_curves[ticker] = equity_curve

results_df = pd.concat(
    {ticker: pd.DataFrame(res) for ticker, res in all_results.items()},
    axis=1
)
results_df = results_df.map(lambda x: f"{x:.2%}" if isinstance(x, float) else x)
print(results_df)

  