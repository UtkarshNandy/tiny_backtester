import pandas

def performance_summary(returns, equity, freq=252):
    ann_return = (equity.iloc[-1] / equity.iloc[0]) ** (freq / len(returns)) - 1
    ann_vol    = returns.std() * (freq ** 0.5)
    sharpe     = ann_return / ann_vol if ann_vol != 0 else 0
    max_dd     = (equity / equity.cummax() - 1).min()
    return {
        "Annual Return": ann_return,
        "Volatility": ann_vol,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": max_dd
    }