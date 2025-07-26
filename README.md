# 📈 Indian Stock Fundamental Analysis Dashboard

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


An interactive web application to analyze Indian stock fundamentals using live financial data from Yahoo Finance. The app provides detailed insights into a company's financials, valuation metrics, cash flows, and technical indicators with sector-wise benchmarking — designed to help investors and analysts make informed decisions.

---

## 🧾 Project Description

**Indian Stock Fundamental Analysis Dashboard** is a user-friendly web application built with **Streamlit** and powered by **Yahoo Finance (yfinance)** that allows investors, analysts, and enthusiasts to perform **fundamental and technical analysis** on Indian stocks listed on the **NSE (National Stock Exchange)**.

The tool fetches real-time financial data, presents it with clean visuals and interactive tabs, and compares company-level metrics with **sector averages** for better insight. It helps users evaluate a stock's financial health, performance, valuation, and growth potential — all from a single dashboard without the need for complex tools or premium data providers.

---

## 🎯 Key Objectives

- Empower Indian investors with **easy access to stock fundamentals**.
- Provide **visual insights** into balance sheets, income statements, cash flows, and technical trends.
- Enable **sector-wise comparisons** using pre-defined stock peer groups.
- Support **retail decision-making** with meaningful metrics like P/E, P/B, Current Ratio, ROE, and Cash Flow Margin.

---

## 📊 Features

- 🔍 **Company Overview**: Market cap, current price, volume, 52-week range, and sector info
- 📈 **Valuation Metrics**: P/E, P/B, PEG, Current Ratio, D/E Ratio, ROE
- 📋 **Financial Statements**: Balance sheet and income statement with visual trends
- 💵 **Cash Flow Analysis**: Operating, investing, and financing cash flows with margin insights
- 📉 **Technical Analysis**: SMA-50/200, candlestick chart, and volume trends
- 🏭 **Sector Benchmarking**: Compare stock Current Ratio with sector average

---

## 🛠️ Tech Stack

| Component     | Technology        |
|---------------|-------------------|
| Language      | Python             |
| UI Framework  | Streamlit          |
| Data Source   | yfinance           |
| Visualization | Plotly, Matplotlib |
| Data Handling | Pandas             |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/indian-stock-analyzer.git
cd indian-stock-analyzer





Create a virtual environment

python -m venv venv
source venv/bin/activate  ## On Windows: venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

requirements.txt
streamlit
yfinance
pandas
plotly
matplotlib

## Usage
streamlit run app.py


🧠 How to Use
Open the app using streamlit run app.py.

Enter a valid NSE stock ticker (e.g., RELIANCE, TCS, HDFCBANK) in the sidebar.

Click “Analyze Stock” to view insights.

Navigate through tabs:

Overview | Valuation | Financials | Cash Flow | Technical

📌 Future Enhancements
Add EPS growth and dividend history

Multi-stock comparisons

Sentiment analysis integration

Export reports as PDF or Excel

🙋 Ideal For
Indian retail investors

Finance students and educators

Market analysts

Investors seeking visual fundamental insights

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements
Streamlit | Yahoo Finance (yfinance) | Plotly | Pandas | Matplotlib




