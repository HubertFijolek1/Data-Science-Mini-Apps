import yfinance as yf
import streamlit as st

"""
# Simple Stock Price App

Shown are the stock closing price and volume of Apple!
"""

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2010-1-1', end = '2021-12-16')
"""
## Closing Price
"""
st.line_chart(tickerDf.Close)
"""
## Volume Price
"""
st.line_chart(tickerDf.Volume)