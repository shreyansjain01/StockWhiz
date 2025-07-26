import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set up the Streamlit app
st.set_page_config(layout="wide", page_title="Indian Stock Fundamental Analyzer")
st.title("🌻 Indian Stock Fundamental Analysis Dashboard")

# Cache sector data to improve performance
@st.cache_data
def get_sector_current_ratio(sector):
    """Returns average current ratio for given sector"""
    # Predefined sector peers
    sector_peers = {
        'Energy': [
            'RELIANCE.NS', 'ONGC.NS', 'IOC.NS', 'BPCL.NS', 'HPCL.NS', 
            'GAIL.NS', 'OIL.NS', 'PETRONET.NS', 'GUJGASLTD.NS', 'MGL.NS',
            'IGL.NS', 'NTPC.NS', 'POWERGRID.NS', 'TATAPOWER.NS', 'ADANIPOWER.NS',
            'TORNTPOWER.NS', 'CESC.NS', 'NHPC.NS', 'SJVN.NS', 'ADANIGREEN.NS',
            'TANLA.NS', 'WEALTH.NS', 'JSWENERGY.NS', 'IREDA.NS', 'COALINDIA.NS',
            'NLCINDIA.NS', 'ADANITRANS.NS', 'TATACOMM.NS', 'ADANIENSOL.NS', 'ADANIGAS.NS'
        ],
        
        'Technology': [
            'INFY.NS', 'TCS.NS', 'WIPRO.NS', 'HCLTECH.NS', 'TECHM.NS',
            'LTIM.NS', 'MPHASIS.NS', 'PERSISTENT.NS', 'COFORGE.NS', 'OFSS.NS',
            'ZENSARTECH.NS', 'MINDTREE.NS', 'LTI.NS', 'HEXAWARE.NS', 'NIITTECH.NS',
            'CYIENT.NS', 'SONATSOFTW.NS', 'TATAELXSI.NS', 'INTELLECT.NS', 'KPITTECH.NS',
            'MASTEK.NS', '3IINFOLTD.NS', 'ROBERT.NS', 'QUESS.NS', 'E2E.NS'
        ],
        
        'Financial Services': [
            'HDFCBANK.NS', 'ICICIBANK.NS', 'SBIN.NS', 'KOTAKBANK.NS', 'AXISBANK.NS',
            'INDUSINDBK.NS', 'BANDHANBNK.NS', 'AUBANK.NS', 'IDFCFIRSTB.NS', 'FEDERALBNK.NS',
            'PNB.NS', 'BANKBARODA.NS', 'CANBK.NS', 'UNIONBANK.NS', 'IOB.NS',
            'HDFC.NS', 'ICICIPRULI.NS', 'SBILIFE.NS', 'HDFCLIFE.NS', 'MAXHEALTH.NS',
            'BAJFINANCE.NS', 'BAJAJFINSV.NS', 'CHOLAFIN.NS', 'MUTHOOTFIN.NS', 'PFC.NS',
            'RECLTD.NS', 'LICHSGFIN.NS', 'SRTRANSFIN.NS', 'L&TFH.NS', 'SHRIRAMFIN.NS'
        ],
        
        'Automobile': [
            'MARUTI.NS', 'TATAMOTORS.NS', 'M&M.NS', 'BAJAJ-AUTO.NS', 'HEROMOTOCO.NS',
            'EICHERMOT.NS', 'BHARATFORG.NS', 'BOSCHLTD.NS', 'TVSMOTOR.NS', 'ASHOKLEY.NS',
            'ESCORTS.NS', 'EXIDEIND.NS', 'AMARAJABAT.NS', 'MRF.NS', 'APOLLOTYRE.NS',
            'JKTYRE.NS', 'CEAT.NS', 'BALKRISIND.NS', 'ENDURANCE.NS', 'SUNDRMFAST.NS',
            'MOTHERSON.NS', 'SONACOMS.NS', 'SUNFLAG.NS', 'WHEELS.NS', 'MAHINDCIE.NS'
        ],
        
        'Pharmaceuticals': [
            'SUNPHARMA.NS', 'DRREDDY.NS', 'CIPLA.NS', 'DIVISLAB.NS', 'BIOCON.NS',
            'LUPIN.NS', 'AUROPHARMA.NS', 'CADILAHC.NS', 'GLENMARK.NS', 'TORNTPHARM.NS',
            'ALKEM.NS', 'NATCOPHARM.NS', 'LAURUSLABS.NS', 'GRANULES.NS', 'JBCHEPHARM.NS',
            'SANOFI.NS', 'PFIZER.NS', 'ABBOTINDIA.NS', 'NIPPV.NS', 'SUVEN.NS',
            'NEULANDLAB.NS', 'FORTIS.NS', 'NARHEDA.NS', 'APLLTD.NS', 'STAR.NS'
        ],
        
        'FMCG': [
            'HINDUNILVR.NS', 'ITC.NS', 'NESTLEIND.NS', 'BRITANNIA.NS', 'DABUR.NS',
            'GODREJCP.NS', 'MARICO.NS', 'COLPAL.NS', 'EMAMILTD.NS', 'PGHH.NS',
            'RADICO.NS', 'UBL.NS', 'MCDOWELL-N.NS', 'UNIONBANK.NS', 'VBL.NS',
            'TATACONSUM.NS', 'JUBLFOOD.NS', 'DALBHARAT.NS', 'PRSMJOHNSN.NS', 'KAJARIACER.NS',
            'BBTC.NS', 'GILLETTE.NS', 'HATSUN.NS', 'KRBL.NS', 'ZYDUSWELL.NS'
        ],
        
        'Metals & Mining': [
            'TATASTEEL.NS', 'JSWSTEEL.NS', 'SAIL.NS', 'HINDALCO.NS', 'VEDL.NS',
            'NMDC.NS', 'COALINDIA.NS', 'HINDZINC.NS', 'JINDALSTEL.NS', 'MOIL.NS',
            'NATIONALUM.NS', 'APLAPOLLO.NS', 'RATNAMANI.NS', 'WELCORP.NS', 'MAHSEAMLES.NS',
            'JSL.NS', 'JSLHISAR.NS', 'RAMCOCEM.NS', 'SHREECEM.NS', 'ULTRACEMCO.NS',
            'ACC.NS', 'AMBUJACEM.NS', 'HEIDELBERG.NS', 'JKLAKSHMI.NS', 'BIRLACORPN.NS'
        ],
        
        'Infrastructure': [
            'LARSEN.NS', 'LT.NS', 'BHEL.NS', 'ADANIPORTS.NS', 'IRB.NS',
            'GMRINFRA.NS', 'GVKPIL.NS', 'NCC.NS', 'PNCINFRA.NS', 'KNRCONST.NS',
            'ASHOKA.NS', 'MBLINFRA.NS', 'HSCL.NS', 'IRCON.NS', 'RITES.NS',
            'GRINFRA.NS', 'ADANIPOWER.NS', 'TATAPOWER.NS', 'NHPC.NS', 'POWERGRID.NS',
            'SJVN.NS', 'TORNTPOWER.NS', 'CESC.NS', 'NLCINDIA.NS', 'JSWENERGY.NS'
        ],
        
        'Telecom': [
            'BHARTIARTL.NS', 'RELIANCE.NS', 'VODAFONE.NS', 'TATACOMM.NS', 'MTNL.NS',
            'ITI.NS', 'HFCL.NS', 'STERLITE.NS', 'TEJASNET.NS', 'OPTOCIRCUI.NS',
            'TATAELXSI.NS', 'TECHM.NS', 'WIPRO.NS', 'HCLTECH.NS', 'INFY.NS'
        ],
        
        'Real Estate': [
            'DLF.NS', 'SOBHA.NS', 'GODREJPROP.NS', 'BRIGADE.NS', 'PRESTIGE.NS',
            'OBEROIRLTY.NS', 'MINDSPACE.NS', 'PHOENIXLTD.NS', 'MAHLIFE.NS', 'SUNTECK.NS',
            'INDIASTSP.NS', 'ASHIANA.NS', 'PURVA.NS', 'KOLTEPATIL.NS', 'MAZDA.NS'
        ],
        
        'Healthcare': [
            'APOLLOHOSP.NS', 'FORTIS.NS', 'NARAYANA.NS', 'MAXHEALTH.NS', 'HCLTECH.NS',
            'METROPOLIS.NS', 'LALPATHLAB.NS', 'THYROCARE.NS', 'DIAGEO.NS', 'SANOFI.NS',
            'PFIZER.NS', 'ABBOTINDIA.NS', 'NIPPV.NS', 'SUVEN.NS', 'NEULANDLAB.NS'
        ],
        
        'Consumer Durables': [
            'TITAN.NS', 'VOLTAS.NS', 'BLUESTARCO.NS', 'WHIRLPOOL.NS', 'HAVELLS.NS',
            'CROMPTON.NS', 'BAJAJELEC.NS', 'VGUARD.NS', 'ORIENTELEC.NS', 'AMBER.NS',
            'IFBIND.NS', 'SUPREMEIND.NS', 'RAJESHEXPO.NS', 'TTKPRESTIG.NS', 'BATAINDIA.NS'
        ],
        
        'Chemicals': [
            'UPL.NS', 'PIIND.NS', 'SRF.NS', 'TATACHEM.NS', 'GNFC.NS',
            'FACT.NS', 'RCF.NS', 'GSFC.NS', 'DEEPAKNTR.NS', 'AARTIIND.NS',
            'ATUL.NS', 'VINATIORGA.NS', 'NAVINFLUOR.NS', 'TANLA.NS', 'WEALTH.NS'
        ],
        
        'Media & Entertainment': [
            'ZEEENT.NS', 'SUNTV.NS', 'DISHTV.NS', 'INOXLEISUR.NS', 'PVR.NS',
            'NETWORK18.NS', 'TV18BRDCST.NS', 'DEN.NS', 'HATHWAY.NS', 'SITINET.NS',
            'BALAJITELE.NS', 'DBREALTY.NS', 'PENINLAND.NS', 'EIHOTEL.NS', 'TAJGVK.NS'
        ]
    }
    
    peers = sector_peers.get(sector, [])
    if not peers:
        return None
    
    ratios = []
    for peer in peers:
        try:
            peer_data = yf.Ticker(peer)
            ratio = peer_data.info.get('currentRatio')
            if ratio:
                ratios.append(ratio)
        except:
            continue
    
    return round(sum(ratios)/len(ratios), 2) if ratios else None
def display_financial_metric(metric, name, unit="Cr"):
    """Helper function to display financial metrics"""
    if metric is None:
        print(f"{name}: Not available")
        return
    
    print(f"\n{name}:")
    if isinstance(metric, pd.Series):
        for date, value in metric.items():
            print(f"{date.date()}: {value/1e7:.2f} {unit}")
    else:
        print(f"{metric/1e7:.2f} {unit}")

# Main analysis function
def analyze_company(ticker):
    info = ticker.info
    balance_sheet = ticker.balance_sheet
    income_stmt = ticker.income_stmt
    cash_flow = ticker.cashflow
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Valuation", "Financials", "Cash Flow", "Technical"])
    
    with tab1:
        st.header("Company Overview")
        
        # Basic info in columns
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Basic Info")
            st.metric("Company", info.get('longName', 'N/A'))
            st.metric("Sector", info.get('sector', 'N/A'))
            st.metric("Industry", info.get('industry', 'N/A'))
        
        with col2:
            st.subheader("Market Data")
            st.metric("Market Cap", f"₹{info.get('marketCap', 0)/1e7:,.2f} Cr" if info.get('marketCap') else 'N/A')
            st.metric("Current Price", f"₹{info.get('currentPrice', 'N/A')}")
            st.metric("52 Week Range", 
                     f"₹{info.get('fiftyTwoWeekLow', 'N/A')} - ₹{info.get('fiftyTwoWeekHigh', 'N/A')}")
        
        with col3:
            st.subheader("Trading Info")
            st.metric("Volume (Avg)", f"{info.get('averageVolume', 0)/1e3:,.1f}K" if info.get('averageVolume') else 'N/A')
            st.metric("Beta", info.get('beta', 'N/A'))
            st.metric("Shares Outstanding", f"{info.get('sharesOutstanding', 0)/1e7:,.2f} Cr" if info.get('sharesOutstanding') else 'N/A')
        
        # Price chart
        st.subheader("Price Movement")
        hist = ticker.history(period="1y")
        if not hist.empty:
            fig = go.Figure()
            fig.add_trace(go.Candlestick(
                x=hist.index,
                open=hist['Open'],
                high=hist['High'],
                low=hist['Low'],
                close=hist['Close'],
                name='Price'
            ))
            fig.update_layout(
                xaxis_rangeslider_visible=False,
                height=500,
                title=f"{ticker.ticker} 1-Year Price Chart"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.header("Valuation Metrics")
        
        # Valuation ratios
        pe_ratio = info.get('trailingPE', 'N/A')
        pb_ratio = info.get('priceToBook', 'N/A')
        curr_ratio = info.get('currentRatio', 'N/A')
        de_ratio = info.get('debtToEquity', 'N/A')
        peg_ratio = info.get('pegRatio', 'N/A')
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Key Ratios")
            st.metric("P/E Ratio", f"{pe_ratio:.2f}" if isinstance(pe_ratio, (int, float)) else pe_ratio)
            st.metric("P/B Ratio", f"{pb_ratio:.2f}" if isinstance(pb_ratio, (int, float)) else pb_ratio)
            st.metric("PEG Ratio", f"{peg_ratio:.2f}" if isinstance(peg_ratio, (int, float)) else peg_ratio)
        
        with col2:
            st.subheader("Financial Health")
            st.metric("Current Ratio", f"{curr_ratio:.2f}" if isinstance(curr_ratio, (int, float)) else curr_ratio)
            st.metric("Debt/Equity", f"{de_ratio:.2f}" if isinstance(de_ratio, (int, float)) else de_ratio)
            st.metric("ROE", f"{info.get('returnOnEquity', 'N/A')}%")
        
        # Valuation chart
        if all(isinstance(x, (int, float)) for x in [pe_ratio, pb_ratio, curr_ratio]):
            fig = px.bar(
                x=['P/E', 'P/B', 'Current'],
                y=[pe_ratio, pb_ratio, curr_ratio],
                text=[f"{pe_ratio:.1f}", f"{pb_ratio:.1f}", f"{curr_ratio:.1f}"],
                title="Key Valuation Ratios"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Sector comparison
        sector = info.get('sector')
        if sector and isinstance(curr_ratio, (int, float)):
            sector_avg = get_sector_current_ratio(sector)
            if sector_avg:
                st.subheader("Sector Comparison")
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=['Company', 'Sector Avg'],
                    y=[curr_ratio, sector_avg],
                    text=[f"{curr_ratio:.2f}", f"{sector_avg:.2f}"],
                    textposition='auto',
                    marker_color=['#636EFA', '#EF553B']
                ))
                fig.update_layout(
                    title=f"Current Ratio Comparison ({sector})",
                    yaxis_title="Current Ratio"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.header("Financial Statements")
        
        # Balance Sheet
        st.subheader("Balance Sheet (₹ in Crores)")
        if not balance_sheet.empty:
            bs_df = balance_sheet.apply(lambda x: round(x / 1e7, 2))  # Convert to crores
            bs_df = bs_df.transpose()
            st.dataframe(bs_df.style.format("{:,.2f}"), use_container_width=True)
            
            # Plot key balance sheet items
            if 'Total Assets' in bs_df.columns and 'Total Liabilities' in bs_df.columns:
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=bs_df.index,
                    y=bs_df['Total Assets'],
                    name='Total Assets',
                    marker_color='#636EFA'
                ))
                fig.add_trace(go.Bar(
                    x=bs_df.index,
                    y=bs_df['Total Liabilities'],
                    name='Total Liabilities',
                    marker_color='#EF553B'
                ))
                fig.update_layout(
                    barmode='group',
                    title="Assets vs Liabilities",
                    yaxis_title="₹ in Crores"
                )
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No balance sheet data available")
        
        # Income Statement
        st.subheader("Income Statement (₹ in Crores)")
        if not income_stmt.empty:
            is_df = income_stmt.apply(lambda x: round(x / 1e7, 2))  # Convert to crores
            is_df = is_df.transpose()
            st.dataframe(is_df.style.format("{:,.2f}"), use_container_width=True)
            
            # Plot revenue and net income
            if 'Total Revenue' in is_df.columns and 'Net Income' in is_df.columns:
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=is_df.index,
                    y=is_df['Total Revenue'],
                    name='Revenue',
                    marker_color='#00CC96'
                ))
                fig.add_trace(go.Bar(
                    x=is_df.index,
                    y=is_df['Net Income'],
                    name='Net Income',
                    marker_color='#AB63FA'
                ))
                fig.update_layout(
                    barmode='group',
                    title="Revenue vs Net Income",
                    yaxis_title="₹ in Crores"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Calculate and plot profit margins
                is_df['Profit Margin'] = (is_df['Net Income'] / is_df['Total Revenue']) * 100
                fig = px.line(
                    is_df,
                    x=is_df.index,
                    y='Profit Margin',
                    title="Net Profit Margin (%)",
                    markers=True
                )
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No income statement data available")
    
    with tab4:
        st.header("Cash Flow Analysis")
        
        if not cash_flow.empty:
            cf_df = cash_flow.apply(lambda x: round(x / 1e7, 2))  # Convert to crores
            cf_df = cf_df.transpose()
            st.dataframe(cf_df.style.format("{:,.2f}"), use_container_width=True)
            
            # Plot cash flow components
            if 'Operating Cash Flow' in cf_df.columns and 'Investing Cash Flow' in cf_df.columns and 'Financing Cash Flow' in cf_df.columns:
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=cf_df.index,
                    y=cf_df['Operating Cash Flow'],
                    name='Operating',
                    marker_color='#00CC96'
                ))
                fig.add_trace(go.Bar(
                    x=cf_df.index,
                    y=cf_df['Investing Cash Flow'],
                    name='Investing',
                    marker_color='#636EFA'
                ))
                fig.add_trace(go.Bar(
                    x=cf_df.index,
                    y=cf_df['Financing Cash Flow'],
                    name='Financing',
                    marker_color='#EF553B'
                ))
                fig.update_layout(
                    barmode='group',
                    title="Cash Flow Components",
                    yaxis_title="₹ in Crores"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Calculate and plot cash flow margin
                if 'Total Revenue' in income_stmt.index:
                    revenue = income_stmt.loc['Total Revenue'] / 1e7  # Convert to crores
                    cf_df['Cash Flow Margin'] = (cf_df['Operating Cash Flow'] / revenue) * 100
                    fig = px.line(
                        cf_df,
                        x=cf_df.index,
                        y='Cash Flow Margin',
                        title="Operating Cash Flow Margin (%)",
                        markers=True
                    )
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No cash flow data available")
    
    with tab5:
        st.header("Technical Analysis")
        
        if not hist.empty:
            # Moving averages
            hist['SMA_50'] = hist['Close'].rolling(window=50).mean()
            hist['SMA_200'] = hist['Close'].rolling(window=200).mean()
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=hist.index,
                y=hist['Close'],
                name='Price',
                line=dict(color='#636EFA')
            ))
            fig.add_trace(go.Scatter(
                x=hist.index,
                y=hist['SMA_50'],
                name='50-Day SMA',
                line=dict(color='#EF553B', dash='dot')
            ))
            fig.add_trace(go.Scatter(
                x=hist.index,
                y=hist['SMA_200'],
                name='200-Day SMA',
                line=dict(color='#00CC96', dash='dot')
            ))
            fig.update_layout(
                title="Price with Moving Averages",
                yaxis_title="Price (₹)",
                hovermode="x unified"
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Volume chart
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=hist.index,
                y=hist['Volume'],
                name='Volume',
                marker_color='#AB63FA'
            ))
            fig.update_layout(
                title="Trading Volume",
                yaxis_title="Volume"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No historical price data available")

# Sidebar for user input
st.sidebar.header("Stock Selection")
ticker_symbol = st.sidebar.text_input("Enter NSE Ticker Symbol (e.g., RELIANCE, TCS)", "RELIANCE").upper()

# Add .NS suffix if not present
if not ticker_symbol.endswith('.NS'):
    ticker_symbol += '.NS'

if st.sidebar.button("Analyze Stock"):
    with st.spinner(f"Fetching data for {ticker_symbol}..."):
        try:
            ticker = yf.Ticker(ticker_symbol)
            # Validate ticker
            if not ticker.info or 'symbol' not in ticker.info:
                st.error(f"Could not find data for {ticker_symbol}. Please check the ticker symbol.")
            else:
                st.success(f"Successfully retrieved data for {ticker.info.get('longName', ticker_symbol)}")
                analyze_company(ticker)
        except Exception as e:
            st.error(f"Error fetching data: {str(e)}")