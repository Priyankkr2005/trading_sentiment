# Trader Performance vs Market Sentiment

## Overview
This project analyzes how Bitcoin market sentiment (Fear/Greed Index) influences trader behavior and performance on Hyperliquid. The goal is to uncover patterns that can inform better trading strategies.

---

## Datasets
1. **Bitcoin Market Sentiment Dataset**
   - Columns: timestamp, value, classification, date
   - Labels: Extreme Fear, Fear, Neutral, Greed, Extreme Greed

2. **Hyperliquid Trader Dataset**
   - Contains trade-level data such as account, execution price, size, side, timestamp, and PnL

---

## Methodology
- Cleaned datasets (handled nulls, duplicates, normalized columns)
- Converted timestamps and aligned both datasets at a **daily level**
- Merged datasets on date
- Computed key metrics:
  - Daily PnL
  - Win rate
  - Trade frequency
  - Average trade size
  - Long/Short ratio
- Performed segmentation:
  - High vs Low trade size
  - Frequent vs Infrequent traders
  - Winners vs Losers

---

## Key Insights
- **Highest profitability during Extreme Greed**  
  Traders achieved the highest PnL (~67.9) and win rate (~46%) in strong bullish sentiment.

- **Risk-taking peaks during Fear but is inefficient**  
  Traders used the largest trade sizes (~7816 USD) during Fear but did not achieve the highest returns.

- **Overtrading reduces profitability**  
  Low-frequency traders outperformed high-frequency traders (95 vs 42 PnL).

- **Position sizing is critical**  
  High trade size segment generated significantly higher returns (92 vs 4 PnL).

---

## Strategy Recommendations
- **Leverage bullish momentum**  
  Increase participation during Extreme Greed using trend-following strategies.

- **Control risk during Fear**  
  Reduce position sizes to avoid inefficient capital allocation.

- **Avoid overtrading**  
  Focus on fewer, high-quality trades rather than frequent execution.

---

## How to Run
# 📊 Trader Performance vs Market Sentiment

## Overview
This project analyzes how Bitcoin market sentiment (Fear/Greed Index) influences trader behavior and performance on Hyperliquid. The goal is to uncover patterns that can inform better trading strategies.

---

## 📁 Datasets
1. **Bitcoin Market Sentiment Dataset**
   - Columns: timestamp, value, classification, date
   - Labels: Extreme Fear, Fear, Neutral, Greed, Extreme Greed

2. **Hyperliquid Trader Dataset**
   - Contains trade-level data such as account, execution price, size, side, timestamp, and PnL

---

## ⚙️ Methodology
- Cleaned datasets (handled nulls, duplicates, normalized columns)
- Converted timestamps and aligned both datasets at a **daily level**
- Merged datasets on date
- Computed key metrics:
  - Daily PnL
  - Win rate
  - Trade frequency
  - Average trade size
  - Long/Short ratio
- Performed segmentation:
  - High vs Low trade size
  - Frequent vs Infrequent traders
  - Winners vs Losers

---

## 📊 Key Insights
- **Highest profitability during Extreme Greed**  
  Traders achieved the highest PnL (~67.9) and win rate (~46%) in strong bullish sentiment.

- **Risk-taking peaks during Fear but is inefficient**  
  Traders used the largest trade sizes (~7816 USD) during Fear but did not achieve the highest returns.

- **Overtrading reduces profitability**  
  Low-frequency traders outperformed high-frequency traders (95 vs 42 PnL).

- **Position sizing is critical**  
  High trade size segment generated significantly higher returns (92 vs 4 PnL).

---

## 🎯 Strategy Recommendations
- **Leverage bullish momentum**  
  Increase participation during Extreme Greed using trend-following strategies.

- **Control risk during Fear**  
  Reduce position sizes to avoid inefficient capital allocation.

- **Avoid overtrading**  
  Focus on fewer, high-quality trades rather than frequent execution.

---

## ▶️ How to Run
1. Install dependencies:
```bash
pip install pandas matplotlib seaborn
1. Install dependencies:
```bash
pip install pandas matplotlib seaborn
