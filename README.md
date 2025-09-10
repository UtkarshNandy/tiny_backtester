This is a tiny backtesting project to get the ball rolling.

Tickers used: SPY, AAPL, MSFT

Bar frequency: Daily

Fill model: Immediate

Costs: 5 BPS / leg


STRATEGY SPECS:

1. Momentum strategy. If price increases, long. If decreases, either short or hold. (Pt / Ptl) - 1
2. Lookback of 20 days.
3. Entry rule: Go long if 20-day momentum > 0
4. Exit rule: Exit if momentum drops below 
5. Max leverage: <= 1 (cash only)
6. Holding period: as long as momentum > 0
7. Rebalance cadence: everyday

BACKTESTING SPECS:

1. Use adjusted close for returns

2. Compute signal from lookback momentum

3. Shift signal by 1 day to create positions

4. Positions ∈ {0, 1} (flat or long), leverage ≤1.

5. Trades = changes in position.

6. Apply transaction cost (5 BPS / leg)

7. Daily P&L = position × daily return – costs

8. Equity = initial capital × cumulative product of (1 + P&L).

PERFORMANCE METRICS:


| Metric                  | Description                                                                 | Formula                                                                                  |
|--------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **CAGR** (Compound Annual Growth Rate) | Smoothed annual growth rate of equity, assuming reinvestment.               | CAGR = (Equity_end / Equity_start)^(252 / N) - 1                                         |
| **Volatility (Vol)**     | Annualized standard deviation of daily returns.                             | Vol = sqrt(252) * StdDev(daily returns)                                                  |
| **Sharpe Ratio (252)**   | Risk-adjusted return per unit of volatility, annualized (252 trading days). | Sharpe = (mean_daily_return / std_daily_return) * sqrt(252)                              |
| **Max Drawdown (MDD)**   | Largest peak-to-trough decline in equity curve.                             | MDD = min_t ( Equity_t / max_{s ≤ t}(Equity_s) - 1 )                                     |
| **Win Rate**             | Fraction of trades that are profitable.                                     | Win Rate = Winning Trades / Total Trades                                                 |
| **Avg Exposure**         | Average fraction of time strategy has an open position.                     | Avg Exposure = (Number of bars with position ≠ 0) / Total Bars                           |
| **Rolling Sharpe**       | Stability check: Sharpe computed over rolling windows (e.g., 6 months).     | Same Sharpe formula, but over rolling window (≈126 trading days)                         |
| **Turnover**             | Frequency of trading; measures capital churn.                               | Turnover = (Sum of absolute position changes) / Number of periods                        |
| **Avg Holding Time**     | Mean number of days a position is held before closing.                      | Avg Holding Time = (Total holding days across trades) / Number of trades                 |
