# 📊 Bitcoin Technical Indicators Dataset

[![Update Status](https://img.shields.io/badge/status-daily%20updated-success)](https://github.com/mouadja02/bitcoin-technical-indicators-dataset)
[![Data Points](https://img.shields.io/badge/data%20points-90%2B%20indicators-blue)](https://github.com/mouadja02/bitcoin-technical-indicators-dataset)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

> A comprehensive, **daily-updated** Bitcoin dataset with OHLCV data and 70+ pre-calculated technical indicators. Perfect for machine learning, algorithmic trading, and financial analysis.

---

## 📈 Dataset Overview

This dataset provides **hourly Bitcoin price data** enriched with a comprehensive suite of technical indicators calculated using TA-Lib. All indicators are pre-calculated and ready for immediate use in your models.

### Key Features

- 🕐 **Hourly granularity** - Detailed intraday data
- 🔄 **Daily updates** - Automated at midnight UTC
- 📊 **70+ indicators** - Moving averages, oscillators, volume, volatility, and more
- 🎯 **ML-ready** - Clean, structured CSV format
- 📉 **Historical data** - Complete Bitcoin trading history
- ⚡ **Production-grade** - Sourced from CryptoCompare API via Snowflake

---

## 📁 Dataset Structure

### File Information

- **Filename**: `bitcoin-hourly-technical-indicators.csv`
- **Format**: CSV (Comma-Separated Values)
- **Encoding**: UTF-8
- **Size**: ~XX MB (varies with historical data)
- **Update Frequency**: Daily at 00:05 UTC

### Data Columns

#### 🕐 Time & Price Data (7 columns)
| Column | Description | Type |
|--------|-------------|------|
| `UNIX_TIMESTAMP` | Unix epoch timestamp | Integer |
| `DATETIME` | ISO 8601 datetime | Timestamp |
| `OPEN` | Opening price (USD) | Float |
| `HIGH` | Highest price (USD) | Float |
| `CLOSE` | Closing price (USD) | Float |
| `LOW` | Lowest price (USD) | Float |
| `VOLUME` | Trading volume (BTC) | Float |

#### 📊 Moving Averages (20 columns)
- **Simple Moving Averages (SMA)**: 5, 10, 20, 50, 100, 200 periods
- **Exponential Moving Averages (EMA)**: 5, 10, 12, 20, 26, 50 periods
- **Weighted Moving Averages (WMA)**: 10, 20 periods
- **Double EMA (DEMA)**: 10, 20 periods
- **Triple EMA (TEMA)**: 10, 20 periods
- **Triangular MA (TRIMA)**: 20 periods
- **Kaufman Adaptive MA (KAMA)**: 20 periods
- **T3 Moving Average**: 5 periods

#### 📉 Momentum Indicators (24 columns)
- **RSI** (Relative Strength Index): 7, 14, 21 periods
- **MACD** (Moving Average Convergence Divergence): MACD, Signal, Histogram
- **Stochastic Oscillator**: SlowK, SlowD, FastK, FastD
- **Stochastic RSI**: FastK, FastD
- **CCI** (Commodity Channel Index): 14, 20 periods
- **CMO** (Chande Momentum Oscillator): 14 periods
- **MOM** (Momentum): 10 periods
- **ROC** (Rate of Change): 10 periods
- **Williams %R**: 14 periods
- **PPO** (Percentage Price Oscillator)
- **APO** (Absolute Price Oscillator)
- **BOP** (Balance of Power)
- **Ultimate Oscillator** (ULTOSC)

#### 📦 Volume Indicators (6 columns)
- **AD** (Accumulation/Distribution)
- **ADOSC** (Chaikin A/D Oscillator)
- **OBV** (On-Balance Volume)
- **MFI** (Money Flow Index): 14 periods

#### 💥 Volatility Indicators (7 columns)
- **Bollinger Bands**: Upper, Middle, Lower
- **ATR** (Average True Range): 14 periods
- **NATR** (Normalized ATR): 14 periods
- **TRANGE** (True Range)
- **TYPPRICE** (Typical Price)

#### 📈 Trend Indicators (13 columns)
- **ADX** (Average Directional Index): 14 periods
- **Directional Indicators**: +DI, -DI, +DM, -DM
- **Aroon Indicator**: Up, Down, Oscillator
- **SAR** (Parabolic SAR)

#### 📐 Statistical Functions (7 columns)
- **BETA** (Beta coefficient)
- **CORREL** (Pearson Correlation)
- **Linear Regression**: Value, Angle, Slope
- **STDDEV** (Standard Deviation)

#### 🌊 Hilbert Transform (5 columns)
- **HT_TRENDMODE** (Trend vs Cycle Mode)
- **HT_SINE** (Sine Wave)
- **HT_LEADSINE** (Lead Sine Wave)
- **HT_TRENDLINE** (Instantaneous Trendline)
- **MAMA** (MESA Adaptive MA)

#### 🕯️ Candlestick Patterns (14 columns)
- Doji, Hammer, Inverted Hammer
- Hanging Man, Shooting Star
- Engulfing, Morning Star, Evening Star
- Three White Soldiers, Three Black Crows
- Harami, Dark Cloud Cover, Piercing
- Marubozu

#### 🎯 Custom Features (5 columns)
- **PRICE_CHANGE** (Absolute price change)
- **HIGH_LOW_RATIO** (High/Low price ratio)
- **CLOSE_OPEN_RATIO** (Close/Open price ratio)
- **VOLATILITY_30D** (30-day rolling volatility)
- **PRICE_VOLATILITY_30D** (30-day price volatility)

---

## 🚀 Quick Start

### Download the Dataset

```bash
# Clone the repository
git clone https://github.com/mouadja02/bitcoin-technical-indicators-dataset.git
cd bitcoin-technical-indicators-dataset

# Or download directly
wget https://raw.githubusercontent.com/mouadja02/bitcoin-technical-indicators-dataset/main/bitcoin-hourly-technical-indicators.csv
```

### Load in Python

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('bitcoin-hourly-technical-indicators.csv')

# Convert datetime
df['DATETIME'] = pd.to_datetime(df['DATETIME'])
df.set_index('DATETIME', inplace=True)

# Display basic info
print(f"Dataset shape: {df.shape}")
print(f"Date range: {df.index.min()} to {df.index.max()}")
print(f"\nFirst few rows:\n{df.head()}")
```

### Quick Analysis Example

```python
import matplotlib.pyplot as plt

# Plot Bitcoin price with moving averages
plt.figure(figsize=(14, 7))
plt.plot(df.index, df['CLOSE'], label='BTC Price', linewidth=1)
plt.plot(df.index, df['SMA_50'], label='SMA 50', linewidth=1.5)
plt.plot(df.index, df['SMA_200'], label='SMA 200', linewidth=1.5)
plt.title('Bitcoin Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# RSI Analysis
plt.figure(figsize=(14, 5))
plt.plot(df.index, df['RSI_14'], label='RSI 14', color='purple')
plt.axhline(y=70, color='r', linestyle='--', label='Overbought')
plt.axhline(y=30, color='g', linestyle='--', label='Oversold')
plt.title('Relative Strength Index (RSI)')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 💡 Use Cases

### 1. Machine Learning Models
```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Prepare features (select relevant indicators)
features = ['SMA_20', 'EMA_12', 'RSI_14', 'MACD', 'BB_UPPER', 
            'BB_LOWER', 'ATR_14', 'OBV', 'ADX_14', 'VOLUME']

X = df[features].dropna()
y = df['CLOSE'].shift(-1).loc[X.index]  # Predict next hour's close

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
score = model.score(X_test, y_test)
print(f"R² Score: {score:.4f}")
```

### 2. Trading Strategy Backtesting
```python
# Simple RSI strategy
df['signal'] = 0
df.loc[df['RSI_14'] < 30, 'signal'] = 1   # Buy signal
df.loc[df['RSI_14'] > 70, 'signal'] = -1  # Sell signal

# Calculate returns
df['returns'] = df['CLOSE'].pct_change()
df['strategy_returns'] = df['signal'].shift(1) * df['returns']

# Performance metrics
total_return = (1 + df['strategy_returns']).cumprod()[-1] - 1
print(f"Strategy Return: {total_return:.2%}")
```

### 3. Feature Engineering
```python
# Create custom features
df['price_momentum'] = df['CLOSE'] / df['SMA_20']
df['volatility_regime'] = pd.qcut(df['ATR_14'], q=3, labels=['Low', 'Medium', 'High'])
df['trend_strength'] = df['ADX_14'] > 25

# Volume analysis
df['volume_ma'] = df['VOLUME'].rolling(20).mean()
df['volume_surge'] = df['VOLUME'] > (df['volume_ma'] * 1.5)
```

### 4. Pattern Recognition
```python
# Find bullish patterns
bullish_patterns = [
    'CDL_HAMMER', 'CDL_INVERTED_HAMMER', 
    'CDL_MORNING_STAR', 'CDL_THREE_WHITE_SOLDIERS'
]

df['bullish_signal'] = df[bullish_patterns].sum(axis=1) > 0

# Find bearish patterns
bearish_patterns = [
    'CDL_SHOOTING_STAR', 'CDL_HANGING_MAN',
    'CDL_EVENING_STAR', 'CDL_THREE_BLACK_CROWS'
]

df['bearish_signal'] = df[bearish_patterns].sum(axis=1) > 0
```

---

## 📊 Data Quality

### Completeness
- ✅ No missing timestamps in sequence
- ✅ All fields are complete (No NULL values)

### Accuracy
- Source: CryptoCompare API
- Calculations: TA-Lib (industry-standard library)
- Validation: Automated daily checks

---

## 🔧 Technical Details

### Data Pipeline Architecture

```
CryptoCompare API → Apache Airflow → Snowflake DWH → GitHub
```

1. **Extraction**: Hourly Bitcoin data from CryptoCompare
2. **Transformation**: Technical indicators calculated using TA-Lib
3. **Loading**: Stored in Snowflake data warehouse
4. **Publishing**: Daily export to GitHub repository

### Update Schedule

- **Frequency**: Daily
- **Time**: 00:05 UTC
- **Automation**: Apache Airflow DAG
- **Notification**: Telegram bot alerts

### Column Naming Convention

- **Uppercase**: All column names are uppercase
- **Underscore**: Words separated by underscores
- **Periods**: Indicator periods specified with underscore (e.g., `RSI_14`)

---

## 📚 Resources

### Technical Indicators Documentation
- [TA-Lib Documentation](https://ta-lib.org/)
- [Investopedia - Technical Indicators](https://www.investopedia.com/terms/t/technicalindicator.asp)
- [TradingView Indicators](https://www.tradingview.com/scripts/)

### Recommended Reading
- **Books**:
  - "Technical Analysis of the Financial Markets" by John Murphy
  - "Python for Finance" by Yves Hilpisch
- **Courses**:
  - Coursera: Machine Learning for Trading
  - Udemy: Algorithmic Trading with Python

### Similar Datasets
- [Yahoo Finance](https://finance.yahoo.com/)
- [CryptoDataDownload](https://www.cryptodatadownload.com/)
- [Kaggle Bitcoin Datasets](https://www.kaggle.com/datasets?search=bitcoin)

---

## ⚠️ Disclaimer

**Important**: This dataset is for educational and research purposes only.

- ❌ **NOT financial advice**
- ❌ **NOT investment recommendations**
- ❌ **NOT guaranteed to be error-free**

Trading cryptocurrencies carries substantial risk. Past performance does not guarantee future results. Always do your own research and consult with financial professionals.

---

## 📄 License

This dataset is released under the **MIT License**.

[![GitHub stars](https://img.shields.io/github/stars/mouadja02/bitcoin-technical-indicators-dataset?style=social)](https://github.com/mouadja02/bitcoin-technical-indicators-dataset)
[![GitHub forks](https://img.shields.io/github/forks/mouadja02/bitcoin-technical-indicators-dataset?style=social)](https://github.com/mouadja02/bitcoin-technical-indicators-dataset)

</div>
