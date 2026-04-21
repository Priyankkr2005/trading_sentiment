import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==============================
# LOAD DATA
# ==============================
sentiment = pd.read_csv("fear_greed_index.csv")
trades = pd.read_csv("historical_data.csv")

# Normalize column names
sentiment.columns = sentiment.columns.str.strip().str.lower()
trades.columns = trades.columns.str.strip().str.lower()

# ==============================
# BASIC CHECKS
# ==============================
print("Sentiment shape:", sentiment.shape)
print("Trades shape:", trades.shape)

print("\nSentiment nulls:\n", sentiment.isnull().sum())
print("\nTrades nulls:\n", trades.isnull().sum())

print("\nSentiment duplicates:", sentiment.duplicated().sum())
print("Trades duplicates:", trades.duplicated().sum())

# ==============================
# DATE ALIGNMENT
# ==============================

sentiment['date'] = pd.to_datetime(sentiment['date']).dt.normalize()

trades['timestamp ist'] = pd.to_datetime(
    trades['timestamp ist'],
    dayfirst=True,
    errors='coerce'
)

trades = trades.dropna(subset=['timestamp ist'])
trades['date'] = trades['timestamp ist'].dt.normalize()

# Keep overlapping dates
min_date = max(trades['date'].min(), sentiment['date'].min())
max_date = min(trades['date'].max(), sentiment['date'].max())

trades = trades[(trades['date'] >= min_date) & (trades['date'] <= max_date)]
sentiment = sentiment[(sentiment['date'] >= min_date) & (sentiment['date'] <= max_date)]

# ==============================
# MERGE
# ==============================
df = pd.merge(
    trades,
    sentiment[['date', 'classification']],
    on='date',
    how='inner'
)

print("\nClassification distribution:\n", df['classification'].value_counts())

# ==============================
# METRICS
# ==============================

df['win'] = df['closed pnl'] > 0
df['date'] = pd.to_datetime(df['date'])

# Daily PnL per trader
daily_pnl = df.groupby(['account', 'date'])['closed pnl'].sum().reset_index()

# Win rate per trader
win_rate = df.groupby('account')['win'].mean().reset_index(name='win_rate')

# Win rate by sentiment (NEW)
win_rate_sentiment = df.groupby('classification')['win'].mean()

# Trades per day
trades_per_day = df.groupby(['account', 'date']).size().reset_index(name='trades_count')

# Avg trade size
avg_position_size = df.groupby('account')['size usd'].mean().reset_index(name='avg_position_size')

# Long/Short ratio
long_short = df.groupby(['account', 'side']).size().unstack(fill_value=0)

# ==============================
# ANALYSIS
# ==============================

pnl_by_sentiment = df.groupby('classification')['closed pnl'].mean()
size_by_sentiment = df.groupby('classification')['size usd'].mean()
trade_count_by_sentiment = df.groupby('classification').size()
long_short_sentiment = pd.crosstab(df['classification'], df['side'])

print("\nPnL by Sentiment:\n", pnl_by_sentiment)
print("\nWin Rate by Sentiment:\n", win_rate_sentiment)
print("\nAvg Trade Size:\n", size_by_sentiment)
print("\nTrade Count:\n", trade_count_by_sentiment)
print("\nLong/Short:\n", long_short_sentiment)

# ==============================
# DRAWDOWN (NEW)
# ==============================

daily_total = df.groupby('date')['closed pnl'].sum().cumsum()
drawdown = daily_total - daily_total.cummax()

print("\nMax Drawdown:", drawdown.min())

# ==============================
# SEGMENTATION (NEW)
# ==============================

# Size segment
median_size = df['size usd'].median()
df['size_segment'] = df['size usd'].apply(lambda x: 'High' if x > median_size else 'Low')

# Frequency segment
trade_freq = df.groupby('account').size()
median_freq = trade_freq.median()

df['freq_segment'] = df['account'].apply(
    lambda x: 'High' if trade_freq[x] > median_freq else 'Low'
)

# Profitability segment
total_pnl = df.groupby('account')['closed pnl'].sum()
df['pnl_segment'] = df['account'].apply(
    lambda x: 'Winner' if total_pnl[x] > 0 else 'Loser'
)

# Segment performance
print("\nSize Segment Performance:\n", df.groupby('size_segment')['closed pnl'].mean())
print("\nFrequency Segment Performance:\n", df.groupby('freq_segment')['closed pnl'].mean())
print("\nPnL Segment Performance:\n", df.groupby('pnl_segment')['closed pnl'].mean())

# ==============================
# VISUALIZATIONS
# ==============================

# 1. PnL Distribution
plt.figure()
sns.boxplot(x='classification', y='closed pnl', data=df)
plt.title("PnL Distribution by Sentiment")
plt.show()

# 2. Trade Size
plt.figure()
size_by_sentiment.plot(kind='bar', title="Avg Trade Size by Sentiment")
plt.show()

# 3. Trade Count
plt.figure()
trade_count_by_sentiment.plot(kind='bar', title="Trade Frequency by Sentiment")
plt.show()

# 4. Long vs Short
plt.figure()
sns.heatmap(long_short_sentiment, annot=True, fmt='d', cmap='coolwarm')
plt.title("Long vs Short by Sentiment")
plt.show()

print("\n✅ FINAL ANALYSIS COMPLETE")