

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





