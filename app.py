
#pip install alpha_vantage
#pip install matplotlib
#pip install tensorflow
#pip install keras
#pip install streamlit
#pip install sklearn
#pip install streamlit-option-menu
#pip install yfinance
#pip install pandas_datareader

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from alpha_vantage.timeseries import TimeSeries
from keras.models import load_model
import streamlit as st
from datetime import datetime
import plotly.express as px
import plotly.graph_objs as go
import yfinance as yf

#for ml model and application project page
st.title('Stock Trend Prediction')
user_input = st.text_input('Enter Stock Ticker' , 'TSLA')

start = st.date_input("Start date (yyyy-mm-dd)", value=pd.to_datetime('2010-01-01'))
end = st.date_input("End date (yyyy-mm-dd)", value=pd.to_datetime('2019-12-31'))

# start = '2010-01-01'
# end = '2019-12-31'
data = yf.download(user_input, start, end)
data.reset_index(inplace=True)
df = pd.DataFrame(data)

#describing data
st.subheader('Data of your Stock')
st.write(df.describe())

#visualization
st.subheader('Closing price vs time chart')
fig = plt.figure(figsize = (12,4))
plt.plot(df.Close)
st.pyplot(fig)

def plot_close_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date,y=df.Close, name="Close", mode='lines'))
    fig.update_layout(title_text='Adjustable Closing price vs time chart with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
plot_close_data()

st.subheader('Closing price vs time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,4))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

def plot_100MA_data():
    ma100 = df.Close.rolling(100).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date,y=df.Close, name="Close", mode='lines'))
    fig.add_trace(go.Scatter(x=df.Date,y=ma100, name="ma100", mode='lines'))
    fig.update_layout(title_text='Ajustable Closing price vs time chart with 100MA', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
plot_100MA_data()

st.subheader('Closing price vs time chart with 100MA and 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize = (12,4))
plt.plot(ma100,'r')
plt.plot(ma200,'g')
plt.plot(df.Close,'b')
st.pyplot(fig)

def plot_200MA_data():
    ma100 = df.Close.rolling(100).mean()
    ma200 = df.Close.rolling(200).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date,y=df.Close, name="Close", mode='lines'))
    fig.add_trace(go.Scatter(x=df.Date,y=ma100, name="ma100", mode='lines'))
    fig.add_trace(go.Scatter(x=df.Date,y=ma200, name="ma200", mode='lines'))
    fig.update_layout(title_text='Adjustable Closing price vs time chart with 100MA and 200MA', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
plot_200MA_data()

# splitting data into training and testing 
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

from sklearn.preprocessing import MinMaxScaler
# Initialize the MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
# Fit and transform the data using the scaler
data_training_array = scaler.fit_transform(data_training)

#load my model
model = load_model('keras_model.hs')

#testing part
past_100_days = data_training.tail(100)
final_df = past_100_days.append(data_testing,ignore_index = True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100,input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i,0])

x_test , y_test = np.array(x_test) , np.array(y_test)

y_predicted = model.predict(x_test)

a=scaler.scale_
scale_factor = 1/a
# scale_factor = 1/scaler.scale_

y_predicted = y_predicted*scale_factor
y_test = y_test*scale_factor

#final graph
st.subheader('Prediction vs Original')
fig2 = plt.figure(figsize = (12,6))
plt.plot(y_test,'y',label = 'Original price')
plt.plot(y_predicted,'g',label = 'Predicted price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)

def plot_predicted_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.Date,y=y_test, name="Original price", mode='lines'))
    fig.add_trace(go.Scatter(x=df.Date,y=y_predicted, name="predicted price", mode='lines'))
    fig.update_layout(title_text='Prediction vs Original', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
plot_predicted_data()


