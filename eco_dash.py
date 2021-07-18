import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st



#### Getting GDP growth rate data by quarter

gdp_gr = pd.read_html('https://www.multpl.com/us-gdp-growth-rate/table/by-quarter', match='Value')[0]

gdp_gr['Date'] = pd.to_datetime(gdp_gr['Date'])

gdp_gr.rename(columns={'Value Value': 'Value'}, inplace=True) 

gdp_gr['Value'] = gdp_gr['Value'].str.strip('%')

gdp_gr['Value'] = pd.to_numeric(gdp_gr['Value'])

gdp_gr.set_index('Date', inplace=True)

gdp_gr = gdp_gr.head(10)

#### Getting US unemployment data by month

unemployment = pd.read_html('https://www.multpl.com/unemployment/table/by-month', match='Rate')[0]

unemployment['Date'] = pd.to_datetime(unemployment['Date'])

unemployment.rename(columns={'Rate Value': 'Value'}, inplace=True)

unemployment['Value'] = unemployment['Value'].str.strip('%')

unemployment['Value'] = pd.to_numeric(unemployment['Value'])

unemployment.set_index('Date', inplace=True)

unemployment = unemployment.head(350)

#### Getting US inflation rate monthly data by month

inflation = pd.read_html('https://www.multpl.com/inflation/table/by-month', match='Value')[0]

inflation['Date'] = pd.to_datetime(inflation['Date'])

inflation.rename(columns={'Value Value': 'Value'}, inplace=True) 

inflation['Value'] = inflation['Value'].str.strip('%')

inflation['Value'] = pd.to_numeric(inflation['Value'])

inflation.set_index('Date', inplace=True)

inflation = inflation.head(50)

## Getting US Retail sales monthly data 

retail = pd.read_html('https://www.multpl.com/us-retail-sales-growth/table/by-month', match='Value')[0]

retail['Date'] = pd.to_datetime(retail['Date'])

retail.rename(columns={'Value Value': 'Value'}, inplace=True) 

retail['Value'] = retail['Value'].str.strip('%')

retail['Value'] = pd.to_numeric(retail['Value'])

retail.set_index('Date', inplace=True)

retail = retail.head(50)

### Getting Shiller P/E 

peshiller = pd.read_html('https://www.multpl.com/shiller-pe/table/by-month', match='Value')[0]

peshiller['Date'] = pd.to_datetime(peshiller['Date'])

peshiller.rename(columns={'Value Value': 'Value'}, inplace=True) 

peshiller['Value'] = pd.to_numeric(peshiller['Value'])

peshiller.set_index('Date', inplace=True)

peshiller = peshiller.head(400)



#### Getting 10Y Treasury yield 

treasury = pd.read_html('https://www.multpl.com/10-year-treasury-rate/table/by-month', match='Value')[0]

treasury['Date'] = pd.to_datetime(treasury['Date'])

treasury.rename(columns={'Value Value': 'Value'}, inplace=True) 

treasury['Value'] = treasury['Value'].str.strip('%')

treasury['Value'] = pd.to_numeric(treasury['Value'])

treasury.set_index('Date', inplace=True)

treasury = treasury.head(20)


#### Getting VIX Index daily price data

vix = yf.Ticker("^VIX")

vixIndex = vix.history(start='2021-01-01', interval='1d')

vixclose = vixIndex['Close']


### Getting Brent oil price daily data 

brent = yf.Ticker("BZ=F")

brentIndex = brent.history(start='2021-01-01')

brentclose = brentIndex['Close']

##### Building the streamlit APP

st.set_page_config(page_title='Key Economic Indicators Dashboard', layout='wide')

header= st.beta_container()

with header:
    st.header('Key Economic Indicators Dashboard')
    st.subheader('The dashboard consists of 7 key indicators to analyse the economic and financial context: Gdp growth, unemployment rate, inflation, Us retail, P/E Shiller, Treasury yield, Vix volatility index and brent oil price')

### First row of indicators: GDP, unemployment, inflation 

gdp, unchart, inflchart = st.beta_columns(3)

plt.style.use('ggplot')

with gdp:
    st.header('   GDP growth rate data by quarter')
    fig1, ax = plt.subplots()
    ax.set_xlabel('Date', labelpad=3.5)
    ax.set_ylabel('Value in %')
    plt.xticks(rotation=-19)
    ax.plot(gdp_gr, marker='.', markersize=10)
    st.pyplot(fig1)

with unchart:
    st.header('   US unemployment data by month')
    fig2, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_ylabel('Value in %')
    ax.plot(unemployment)
    st.pyplot(fig2)

with inflchart:
    st.header('  US inflation rate monthly data by month')
    fig3, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_ylabel('Value in %')
    plt.xticks(rotation=-19)
    ax.plot(inflation, marker='.', markersize=10)
    st.pyplot(fig3)

st.markdown('<hr>', unsafe_allow_html=True)

### Second row of indicators: US Retail sales monthly data, Shiller P/E, 10Y Treasury yield

retus, shiller, treas = st.beta_columns(3)

with retus:
    st.header('US retail monthly data')
    fig4, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    plt.xticks(rotation=-19)
    ax.plot(retail, marker='.', markersize=10)
    st.pyplot(fig4)

with shiller:
    st.header('P/E Shiller - S&P 500')
    fig5, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.plot(peshiller, marker='.', markersize=7)
    st.pyplot(fig5)

with treas:
    st.header(' 10y Treasury Yield')
    fig6, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_ylabel('Yield in %')
    plt.xticks(rotation=-19)
    ax.plot(treasury, marker='.', markersize=10)
    st.pyplot(fig6)

st.markdown('<hr>', unsafe_allow_html=True)

### Third row of indicators: VIX Index, Brent oil

vol, oil = st.beta_columns(2)

with vol:
    st.header('Vix Volatility Index')
    fig7, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    ax.plot(vixclose)
    st.pyplot(fig7)

with oil:
    st.header(' Brent Oil Price Index')
    fig8, ax = plt.subplots()
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.plot(brentclose)
    st.pyplot(fig8)