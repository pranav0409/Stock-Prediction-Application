import streamlit as st
from datetime import date, timedelta
import pandas as pd
import numpy as np
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import plotly.express as px
import plotly.graph_objs as go
import statsmodels.api as sm
import matplotlib.pyplot as plt

START = "2010-01-01"
# TODAY = "2023-02-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')
stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)
# n_years = st.slider('Years of prediction:', 1, 5)
# period = int(n_years * 365)
period=1
@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')
df = pd.DataFrame(data)
st.subheader('Raw data')
st.write(df.tail(10))

# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date, y=df.Open, name="Open", mode='lines'))
    fig.add_trace(go.Scatter(x=df.Date, y=df.Close, name="Close", mode='lines'))
    fig.update_layout(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
plot_raw_data()

df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": 'y'})
df_train['ds'] = pd.to_datetime(df_train['ds'])
df_train = df_train.set_index('ds')

# Specify the frequency of the time series data
df_train = df_train.asfreq('D')

# st.write("Trying to fit the ARIMA model")
model = sm.tsa.ARIMA(df_train, order=(5, 1, 0))
model_fit = model.fit()
# st.write("Successfully fitted the ARIMA model")
#----------------------------------------------------
def arima_forecast(data, order, horizon):
    model = sm.tsa.ARIMA(data, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=horizon)
    return forecast[0]
def cross_validate_arima(data, order, horizon, num_folds=5):
    k = len(data) // num_folds
    forecasts = []
    for i in range(num_folds):
        test_start = i * k
        test_end = (i + 1) * k
        test_data = data.iloc[test_start:test_end]

order =(5,1,0)
#arima_forecast(data,order,period)
#forecast = cross_validate_arima(df_train, order, period, 5)
# st.write("Forecasting values for the next " + str(n_years) + " years")
forecast = model_fit.forecast(steps=period)
df_forecast = pd.DataFrame({'y_pred': forecast[0]},
                           index=pd.date_range(df_train.index[-1]+pd.Timedelta(days=1),
                                               df_train.index[-1]+pd.Timedelta(days=2)))

# Show and plot forecast
st.subheader('Forecast data')
st.write(df_forecast.tail(1))

# st.write(f'Forecast plot for {n_years} years')
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_forecast.index, y=df_forecast['y_pred'], name='Forecast', mode='lines'))
fig.add_trace(go.Scatter(x=df_train.index, y=df_train['y'], name='Actual', mode='lines'))
fig.update_layout(title_text='ARIMA Forecast')
st.plotly_chart(fig)