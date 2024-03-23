import streamlit as st
import pandas as pd 
from dummies import * 
import joblib 

model=joblib.load('model.h5')
#scaler=joblib.load('scaler.h5')

st.title('Bikes Renting Streamlit App')
st.info('just building a testing app for out ml model ')

col1,col2,col3=st.columns(3)
col1.metric('temp','234')
col2.metric('humidity','2345')
col3.metric('weather','clear')


temp=st.number_input('Enter Temperature: ')
humidity=st.number_input('Enter humidity: ')
hour=st.slider('Hour? ',0,24,15)
is_rush_hour=st.selectbox('Is Rush Hour or Not? ',[0,1])
month=st.slider('Month? ', 1,12,5)
season_selection=st.selectbox('Season? ',['winter','spring','summer','fall'])
season=season_dummies[season_selection]
weather_selection=st.selectbox('Weather? ',['clear', 'mist', 'rainy','snowy'])
weather=weather_dummies[weather_selection]
week_day_selection=st.selectbox('week_day? ',['saturday','sunday','monday','tuesday','wednesday','thursday','friday'])
week_day=weekdays_dummies[week_day_selection]
pod_selection=st.selectbox('Period of Day? ',['evening','morning','night','afternoon'])
pod=pod_dummies[pod_selection]


data=[temp,humidity,hour,is_rush_hour,month]
data=data+season+weather+week_day+pod

st.write(data)

#data_scaled=scaler.transform([data])
#result=model.predict(data_scaled)

result=model.predict([data])

st.write(result)
