import yfinance as yf


data = yf.download(
  ["AAPL", "MSFT", "SPY"],
  "2021-01-01",
  "2025-01-01",
  interval="1d",
  group_by="ticker",
  auto_adjust="True"
)

data.drop_duplicates()
appl_data = data["SPY"]
print(appl_data)
