from metrics import performance_summary

def run_momentum_strategy(prices, L=20, cost_rate=.0005):
  """
    Run momentum backtest on a given price series.
    
    prices: pd.Series of adjusted close prices
    L: lookback period (days)
    cost_rate: transaction cost per trade
    """
  
  daily_returns = prices.pct_change().fillna(0)

  momentum = (prices / prices.shift(L)) - 1
  signal = (momentum > 0).astype(int)
  position = signal.shift(1).fillna(0)
  trade = position.diff().fillna(0)
  cost = trade.abs() * .0005 # .05 abs / leg
  pnl_net = position * daily_returns - cost
  equity_curve = 100 * (1 + pnl_net).cumprod()

  train_returns = pnl_net.loc["2005-01-03":"2015-12-31"]
  test_returns  = pnl_net.loc["2017-01-01":"2025-01-01"]

  train_equity = equity_curve.loc["2005-01-03":"2015-12-31"]
  test_equity  = equity_curve.loc["2017-01-01":"2025-01-01"]

  results = {
        "Train": performance_summary(train_returns, train_equity),
        "Test": performance_summary(test_returns, test_equity)
  }

  return equity_curve, results