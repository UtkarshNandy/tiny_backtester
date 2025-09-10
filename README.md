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

1. CAGR: compounded annual growth rate. (Ending equity / starting equity)^(252/N) - 1, n = trading days126.097

2. Volatility - Risk. Annualized standard deviation of risks. Vol = 252^.5 * StdDev(daily returns)

3. Sharpe ratio - risk adjusted returns. Mean(daily returns) / stdDev(daily returns) * 252^.5

4. Max drawdown - Largest peak to trough equity drop 

5. Win rate

6. Avg exposure 

| **Metric**                             | **Definition**                                                              | **Formula**                                                                                                                |                        |                      |
| -------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------- | -------------------- |
| **CAGR** (Compound Annual Growth Rate) | Smoothed annual growth rate of equity, assuming reinvestment.               | $\text{CAGR} = \left(\frac{\text{Equity}_{\text{end}}}{\text{Equity}_{\text{start}}}\right)^{\tfrac{252}{N}} - 1$          |                        |                      |
| **Volatility (Vol)**                   | Annualized standard deviation of daily returns.                             | $\text{Vol} = \sqrt{252} \cdot \text{StdDev}(\text{daily returns})$                                                        |                        |                      |
| **Sharpe Ratio (252)**                 | Risk-adjusted return per unit of volatility, annualized (252 trading days). | $\text{Sharpe} = \frac{\mu_{\text{daily}}}{\sigma_{\text{daily}}} \cdot \sqrt{252}$                                        |                        |                      |
| **Max Drawdown (MDD)**                 | Largest peak-to-trough decline in equity curve.                             | $\text{MDD} = \min_t \left(\frac{\text{Equity}_t - \max_{s \leq t}\text{Equity}_s}{\max_{s \leq t}\text{Equity}_s}\right)$ |                        |                      |
| **Win Rate**                           | Fraction of trades that are profitable.                                     | $\text{Win Rate} = \tfrac{\# \text{Winning Trades}}{\ \text{Total Trades}}$                                               |                        |                      |
| **Avg Exposure**                       | Average fraction of time strategy has an open position.                     | $\text{Avg Exposure} = \tfrac{\sum (\text{position} \neq 0)}{\text{Total Bars}}$                                           |                        |                      |
| **Rolling Sharpe**                     | Stability check: Sharpe computed over rolling windows (e.g., 6 months).     | Same Sharpe formula, but over window (≈126 trading days).                                                                  |                        |                      |
| **Turnover**                           | Frequency of trading; measures capital churn.                               | (\text{Turnover} = \tfrac{\sum                                                                                             | \Delta \text{Position} | }{\text{# periods}}) |
| **Avg Holding Time**                   | Mean number of days a position is held before closing.                      | $\text{Avg Holding Time} = \tfrac{\sum \text{holding days per trade}}{\ \text{trades}}$                                   |                        |                      |
