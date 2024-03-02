#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import yfinance as yf
import datetime
st.title('Welcome to Stock World')
stock_ticker = st.text_input('Stock Chooser','GOOG')



col1, col2 = st.columns(2)
with col1:
    date1 = st.date_input("Start Date", value=None)

with col2:
    date1 = st.date_input("End Date", value=None)  
    
    

msft = yf.Ticker(stock_ticker)
hist = msft.history(period="1mo")


# st.line_chart(hist['Volume'])
col1, col2 = st.columns(2)
with col1:
    st.header("Close Value")
    st.line_chart(hist['Close'])
with col2:
    st.header("Volumes")
    st.line_chart(hist['Volume'])

#Author Abhishek Mishra





