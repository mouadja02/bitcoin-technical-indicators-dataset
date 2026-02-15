"""
Bitcoin Technical Indicators Calculator
========================================

This script demonstrates how to calculate 90+ technical indicators
using TA-Lib on Bitcoin OHLCV data.

Requirements:
    pip install pandas numpy ta-lib

Usage:
    python calculate_technical_indicators.py

Input:
    - CSV file with columns: UNIX_TIMESTAMP, DATETIME, OPEN, HIGH, CLOSE, LOW, VOLUME (or VOLUME_USD)

Output:
    - CSV file with OHLCV + 90+ technical indicators
"""

import pandas as pd
import numpy as np
import talib


def load_ohlcv_data(filepath='bitcoin-hourly-ohlcv.csv'):
    # Load OHLCV data from CSV file
    
    print(f"📥 Loading data from {filepath}...")
    df = pd.read_csv(filepath)
    
    # Ensure datetime column exists
    if 'DATETIME' not in df.columns and 'UNIX_TIMESTAMP' in df.columns:
        df['DATETIME'] = pd.to_datetime(df['UNIX_TIMESTAMP'], unit='s')
    
    print(f"✅ Loaded {len(df):,} records")
    return df


def calculate_technical_indicators(df):
    # Calculate comprehensive technical indicators using TA-Lib

    print("🔧 Calculating comprehensive technical indicators using TA-Lib...")
    
    # Convert to numpy arrays for TA-Lib
    open_prices = df['OPEN'].values
    high_prices = df['HIGH'].values
    low_prices = df['LOW'].values
    close_prices = df['CLOSE'].values
    volume = df['VOLUME'].values
    
    # Dictionary to store all new columns (more efficient than adding one by one)
    new_columns = {}
    
    # ========== OVERLAP STUDIES (Moving Averages) ==========
    print("  📊 Calculating Moving Averages...")
    
    # Simple Moving Averages
    new_columns['SMA_5'] = talib.SMA(close_prices, timeperiod=5)
    new_columns['SMA_10'] = talib.SMA(close_prices, timeperiod=10)
    new_columns['SMA_20'] = talib.SMA(close_prices, timeperiod=20)
    new_columns['SMA_50'] = talib.SMA(close_prices, timeperiod=50)
    new_columns['SMA_100'] = talib.SMA(close_prices, timeperiod=100)
    new_columns['SMA_200'] = talib.SMA(close_prices, timeperiod=200)
    
    # Exponential Moving Averages
    new_columns['EMA_5'] = talib.EMA(close_prices, timeperiod=5)
    new_columns['EMA_10'] = talib.EMA(close_prices, timeperiod=10)
    new_columns['EMA_12'] = talib.EMA(close_prices, timeperiod=12)
    new_columns['EMA_20'] = talib.EMA(close_prices, timeperiod=20)
    new_columns['EMA_26'] = talib.EMA(close_prices, timeperiod=26)
    new_columns['EMA_50'] = talib.EMA(close_prices, timeperiod=50)
    
    # Weighted Moving Averages
    new_columns['WMA_10'] = talib.WMA(close_prices, timeperiod=10)
    new_columns['WMA_20'] = talib.WMA(close_prices, timeperiod=20)
    
    # Double & Triple Exponential Moving Averages
    new_columns['DEMA_10'] = talib.DEMA(close_prices, timeperiod=10)
    new_columns['DEMA_20'] = talib.DEMA(close_prices, timeperiod=20)
    new_columns['TEMA_10'] = talib.TEMA(close_prices, timeperiod=10)
    new_columns['TEMA_20'] = talib.TEMA(close_prices, timeperiod=20)
    
    # Other Moving Averages
    new_columns['TRIMA_20'] = talib.TRIMA(close_prices, timeperiod=20)
    new_columns['KAMA_20'] = talib.KAMA(close_prices, timeperiod=20)
    new_columns['T3_5'] = talib.T3(close_prices, timeperiod=5)
    
    # Bollinger Bands
    new_columns['BB_UPPER'], new_columns['BB_MIDDLE'], new_columns['BB_LOWER'] = talib.BBANDS(close_prices, timeperiod=20)
    
    # ========== MOMENTUM INDICATORS ==========
    print("  📈 Calculating Momentum Indicators...")
    
    # RSI (Relative Strength Index)
    new_columns['RSI_7'] = talib.RSI(close_prices, timeperiod=7)
    new_columns['RSI_14'] = talib.RSI(close_prices, timeperiod=14)
    new_columns['RSI_21'] = talib.RSI(close_prices, timeperiod=21)
    
    # MACD
    new_columns['MACD'], new_columns['MACD_SIGNAL'], new_columns['MACD_HIST'] = talib.MACD(close_prices)
    
    # Stochastic Oscillators
    new_columns['SLOWK'], new_columns['SLOWD'] = talib.STOCH(high_prices, low_prices, close_prices)
    new_columns['FASTK'], new_columns['FASTD'] = talib.STOCHF(high_prices, low_prices, close_prices)
    
    # Stochastic RSI
    new_columns['STOCHRSI_FASTK'], new_columns['STOCHRSI_FASTD'] = talib.STOCHRSI(close_prices)
    
    # Commodity Channel Index
    new_columns['CCI_14'] = talib.CCI(high_prices, low_prices, close_prices, timeperiod=14)
    new_columns['CCI_20'] = talib.CCI(high_prices, low_prices, close_prices, timeperiod=20)
    
    # Other Momentum Indicators
    new_columns['CMO_14'] = talib.CMO(close_prices, timeperiod=14)
    new_columns['MOM_10'] = talib.MOM(close_prices, timeperiod=10)
    new_columns['ROC_10'] = talib.ROC(close_prices, timeperiod=10)
    new_columns['ROCP_10'] = talib.ROCP(close_prices, timeperiod=10)
    new_columns['ROCR_10'] = talib.ROCR(close_prices, timeperiod=10)
    new_columns['WILLR_14'] = talib.WILLR(high_prices, low_prices, close_prices, timeperiod=14)
    new_columns['PPO'] = talib.PPO(close_prices)
    new_columns['APO'] = talib.APO(close_prices)
    new_columns['BOP'] = talib.BOP(open_prices, high_prices, low_prices, close_prices)
    new_columns['ULTOSC'] = talib.ULTOSC(high_prices, low_prices, close_prices)
    
    # ========== VOLUME INDICATORS ==========
    print("  📊 Calculating Volume Indicators...")
    
    new_columns['AD'] = talib.AD(high_prices, low_prices, close_prices, volume)
    new_columns['ADOSC'] = talib.ADOSC(high_prices, low_prices, close_prices, volume)
    new_columns['OBV'] = talib.OBV(close_prices, volume)
    new_columns['MFI_14'] = talib.MFI(high_prices, low_prices, close_prices, volume, timeperiod=14)
    
    # ========== VOLATILITY INDICATORS ==========
    print("  📉 Calculating Volatility Indicators...")
    
    new_columns['ATR_14'] = talib.ATR(high_prices, low_prices, close_prices, timeperiod=14)
    new_columns['NATR_14'] = talib.NATR(high_prices, low_prices, close_prices, timeperiod=14)
    new_columns['TRANGE'] = talib.TRANGE(high_prices, low_prices, close_prices)
    
    # ========== PRICE TRANSFORM ==========
    print("  💰 Calculating Price Transforms...")
    
    new_columns['AVGPRICE'] = talib.AVGPRICE(open_prices, high_prices, low_prices, close_prices)
    new_columns['MEDPRICE'] = talib.MEDPRICE(high_prices, low_prices)
    new_columns['TYPPRICE'] = talib.TYPPRICE(high_prices, low_prices, close_prices)
    new_columns['WCLPRICE'] = talib.WCLPRICE(high_prices, low_prices, close_prices)
    
    # ========== TREND INDICATORS ==========
    print("  📈 Calculating Trend Indicators...")
    
    # ADX (Average Directional Index)
    new_columns['ADX_14'] = talib.ADX(high_prices, low_prices, close_prices, timeperiod=14)
    new_columns['ADXR_14'] = talib.ADXR(high_prices, low_prices, close_prices, timeperiod=14)
    new_columns['DX_14'] = talib.DX(high_prices, low_prices, close_prices, timeperiod=14)
    
    # Directional Movement
    new_columns['MINUS_DI'] = talib.MINUS_DI(high_prices, low_prices, close_prices, timeperiod=14)
    new_columns['PLUS_DI'] = talib.PLUS_DI(high_prices, low_prices, close_prices, timeperiod=14)
    new_columns['MINUS_DM'] = talib.MINUS_DM(high_prices, low_prices, timeperiod=14)
    new_columns['PLUS_DM'] = talib.PLUS_DM(high_prices, low_prices, timeperiod=14)
    
    # Aroon Indicator
    new_columns['AROON_DOWN'], new_columns['AROON_UP'] = talib.AROON(high_prices, low_prices, timeperiod=14)
    new_columns['AROONOSC'] = talib.AROONOSC(high_prices, low_prices, timeperiod=14)
    
    # Parabolic SAR
    new_columns['SAR'] = talib.SAR(high_prices, low_prices)
    
    # ========== STATISTICAL FUNCTIONS ==========
    print("  📊 Calculating Statistical Functions...")
    
    new_columns['BETA'] = talib.BETA(high_prices, low_prices, timeperiod=5)
    new_columns['CORREL'] = talib.CORREL(high_prices, low_prices, timeperiod=30)
    new_columns['LINEARREG'] = talib.LINEARREG(close_prices, timeperiod=14)
    new_columns['LINEARREG_ANGLE'] = talib.LINEARREG_ANGLE(close_prices, timeperiod=14)
    new_columns['LINEARREG_INTERCEPT'] = talib.LINEARREG_INTERCEPT(close_prices, timeperiod=14)
    new_columns['LINEARREG_SLOPE'] = talib.LINEARREG_SLOPE(close_prices, timeperiod=14)
    new_columns['STDDEV'] = talib.STDDEV(close_prices, timeperiod=20)
    new_columns['TSF'] = talib.TSF(close_prices, timeperiod=14)
    new_columns['VAR'] = talib.VAR(close_prices, timeperiod=20)
    
    # ========== HILBERT TRANSFORM (Cycle Indicators) ==========
    print("  🌊 Calculating Hilbert Transform Indicators...")
    
    new_columns['HT_DCPERIOD'] = talib.HT_DCPERIOD(close_prices)
    new_columns['HT_DCPHASE'] = talib.HT_DCPHASE(close_prices)
    new_columns['HT_TRENDMODE'] = talib.HT_TRENDMODE(close_prices)
    new_columns['HT_SINE'], new_columns['HT_LEADSINE'] = talib.HT_SINE(close_prices)
    new_columns['HT_INPHASE'], new_columns['HT_QUADRATURE'] = talib.HT_PHASOR(close_prices)
    new_columns['HT_TRENDLINE'] = talib.HT_TRENDLINE(close_prices)
    
    # MESA Adaptive Moving Average
    new_columns['MAMA'], new_columns['FAMA'] = talib.MAMA(close_prices)
    
    # ========== CANDLESTICK PATTERNS ==========
    print("  🕯️  Calculating Candlestick Patterns...")
    
    new_columns['CDL_DOJI'] = talib.CDLDOJI(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_HAMMER'] = talib.CDLHAMMER(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_INVERTED_HAMMER'] = talib.CDLINVERTEDHAMMER(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_HANGING_MAN'] = talib.CDLHANGINGMAN(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_SHOOTING_STAR'] = talib.CDLSHOOTINGSTAR(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_ENGULFING'] = talib.CDLENGULFING(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_MORNING_STAR'] = talib.CDLMORNINGSTAR(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_EVENING_STAR'] = talib.CDLEVENINGSTAR(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_THREE_WHITE_SOLDIERS'] = talib.CDL3WHITESOLDIERS(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_THREE_BLACK_CROWS'] = talib.CDL3BLACKCROWS(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_HARAMI'] = talib.CDLHARAMI(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_DARK_CLOUD_COVER'] = talib.CDLDARKCLOUDCOVER(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_PIERCING'] = talib.CDLPIERCING(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_MARUBOZU'] = talib.CDLMARUBOZU(open_prices, high_prices, low_prices, close_prices)
    new_columns['CDL_SPINNING_TOP'] = talib.CDLSPINNINGTOP(open_prices, high_prices, low_prices, close_prices)
    
    # ========== CUSTOM FEATURES ==========
    print("  🔧 Calculating Custom Features...")
    
    # Price change percentage
    new_columns['PRICE_CHANGE'] = close_prices / np.roll(close_prices, 1) - 1
    
    # Ratios
    new_columns['HIGH_LOW_RATIO'] = high_prices / low_prices
    new_columns['CLOSE_OPEN_RATIO'] = close_prices / open_prices
    
    # 30-day volatility features (720 hours = 30 days for hourly data)
    window = 720
    new_columns['VOLATILITY_30D'] = pd.Series(new_columns['PRICE_CHANGE']).rolling(window=window).std() * np.sqrt(24)
    new_columns['PRICE_VOLATILITY_30D'] = pd.Series(close_prices).rolling(window=window).std()
    new_columns['HL_VOLATILITY_30D'] = pd.Series((high_prices - low_prices) / close_prices).rolling(window=window).mean()
    
    # Merge all new columns at once (avoids DataFrame fragmentation)
    df_result = pd.concat([df, pd.DataFrame(new_columns, index=df.index)], axis=1)
    
    print(f"✅ Calculated {len(new_columns)} technical indicators")
    print(f"📊 Total columns: {len(df_result.columns)}")
    
    return df_result


def save_to_csv(df, filepath='bitcoin-hourly-technical-indicators.csv'):
    # Save DataFrame to CSV file
    print(f"💾 Saving to {filepath}...")
    df.to_csv(filepath, index=False, float_format='%.8f')
    print(f"✅ Saved {len(df):,} records to {filepath}")


def main():  
    # Step 1: Load OHLCV data
    df = load_ohlcv_data('bitcoin-hourly-ohlcv.csv')
    print()
    
    # Step 2: Calculate technical indicators
    df_with_indicators = calculate_technical_indicators(df)
    print()
    
    # Step 3: Save to CSV
    save_to_csv(df_with_indicators, 'bitcoin-hourly-technical-indicators.csv')
    print()


if __name__ == "__main__":
    main()
