# StockWhiz
# 📈 Indian Stock Fundamental Analysis Dashboard

This is an interactive Streamlit web application that provides a comprehensive **fundamental and technical analysis** dashboard for Indian publicly traded companies listed on the NSE (National Stock Exchange of India).

![Dashboard Preview](https://img.shields.io/badge/Built%20With-Streamlit-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Features

- 🔍 **Stock Overview**  
  Get basic company details, sector, industry, and market stats like market cap, 52-week range, and average volume.

- 📊 **Valuation Metrics**  
  View important valuation ratios like P/E, P/B, PEG, Current Ratio, Debt/Equity, and ROE. Includes sector comparison for current ratio.

- 📑 **Financial Statements**  
  Analyze the balance sheet and income statement, both in tabular and visual formats (e.g., revenue vs. net income, assets vs. liabilities).

- 💰 **Cash Flow Analysis**  
  Track operating, investing, and financing cash flows along with operating cash flow margins.

- 📉 **Technical Analysis**  
  View 1-year candlestick chart, moving averages (SMA-50 and SMA-200), and trading volume charts.

## 🧠 How It Works

The app uses the [yfinance](https://github.com/ranaroussi/yfinance) API to fetch real-time and historical financial data for Indian stocks. It processes this data and presents it using interactive charts and tables with [Plotly](https://plotly.com/python/) and Streamlit.

## 🛠️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/indian-stock-analyzer.git
cd indian-stock-analyzer
