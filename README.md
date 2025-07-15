# Bitcoin Price Hourly Tracker

This repository maintains Bitcoin hourly price data from 2015 to present, using a combination of historical data files and daily backups. A workflow fetches current data from CryptoCompare and stores it in Snowflake, and at the end of the day creates daily CSV backups on GitHub.
Data is collected from CryptoCompare API
An advanced version of this dataset is available on: https://www.kaggle.com/datasets/mouadjaouhari/bitcoin-hourly-ohclv-dataset

## Data Structure
Bitcoin price data is stored with the following schema:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| TIME_UNIX   | INTEGER   | Unix timestamp for the hourly data point |
| DATE_STR    | DATE      | Date in YYYY-MM-DD format |
| HOUR_STR    | VARCHAR   | Hour in 24-hour format (00-23) |
| OPEN_PRICE  | FLOAT     | Opening price for the hour |
| HIGH_PRICE  | FLOAT     | Highest price during the hour |
| CLOSE_PRICE | FLOAT     | Closing price for the hour |
| LOW_PRICE   | FLOAT     | Lowest price during the hour |
| VOLUME_FROM | FLOAT     | Volume in BTC |
| VOLUME_TO   | FLOAT     | Volume in USD |

## Data License and Use
This dataset is free to use and is specifically designed for machine learning projects and research purposes. You're welcome to use this data for academic research, training ML models, educational purposes, and non-commercial applications. Attribution is appreciated but not required. 

## License 📄
This project is licensed under the MIT License - see the LICENSE file for details.
