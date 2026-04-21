# 📊 Trader Performance vs Market Sentiment

## 🚀 Key Results
- **Extreme Greed → highest profitability** (PnL ≈ 67.9, Win Rate ≈ 46%)
- **Fear → highest risk-taking** (avg trade size ≈ 7816 USD) but not highest returns
- **Low-frequency traders outperform high-frequency traders (~95 vs 42 PnL)**
- **Position size strongly impacts returns (~92 vs 4 PnL)**

---

## 📁 Datasets
1. **Bitcoin Market Sentiment (Fear/Greed Index)**
   - Columns: timestamp, value, classification, date

2. **Hyperliquid Trader Data**
   - Trade-level data: account, execution price, size, side, timestamp, closed PnL, etc.

---

## ⚙️ Data Preparation
- Sentiment dataset: **2644 rows, 4 columns**
- Trades dataset: **211,224 rows, 16 columns**
- Missing values: **None**
- Duplicates: **None**

### Processing Steps
- Normalized column names
- Converted timestamps (IST) with `dayfirst=True`
- Aligned both datasets at **daily level**
- Filtered overlapping date range
- Merged on date

> Note: Leverage data was unavailable; **trade size (USD)** is used as a proxy for risk.

---

## 📊 Metrics Computed
- Daily PnL per trader
- Win rate
- Average trade size
- Trades per day
- Long/Short ratio

---

## ❓ Answers to Key Questions

### Does performance differ across sentiment?
✔ Yes  
- Extreme Greed → highest PnL and win rate  
- Fear → high activity but lower efficiency  

### Do traders change behavior?
✔ Yes  
- Larger trade sizes during Fear  
- More trades during Fear  
- Slight short bias during Greed  

---

## 📉 Drawdown
- Maximum drawdown: **-419,020**
- Indicates periods of significant downside risk

---

## 🔍 Segment Analysis

### 1. Trade Size
- High size → **92 PnL**
- Low size → **4 PnL**

### 2. Trading Frequency
- Low-frequency → **95 PnL**
- High-frequency → **42 PnL**

### 3. Profitability
- Winners → positive average PnL
- Losers → negative PnL

---

## 📈 Key Insights

1. **Profitability peaks in bullish sentiment**
   - Extreme Greed yields highest PnL and win rate

2. **Risk-taking is inefficient during Fear**
   - Largest positions but not highest returns

3. **Overtrading reduces profitability**
   - Low-frequency traders outperform significantly

4. **Capital allocation matters more than frequency**
   - Trade size has a stronger impact on returns

---

## 🎯 Strategy Recommendations

1. **Leverage bullish momentum**
   - Increase exposure during Extreme Greed

2. **Control risk during Fear**
   - Reduce position size by ~25–30%

3. **Avoid overtrading**
   - Focus on fewer, high-quality trades

---

## ▶️ How to Run

### Requirements
- pandas
- matplotlib
- seaborn

### Run
```bash
python a1.py
