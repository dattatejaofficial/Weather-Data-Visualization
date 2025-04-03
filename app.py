import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import express as px
import requests
from geopy.geocoders import Nominatim
from datetime import datetime

load_dotenv()

api_key = os.getenv('API_KEY')

st.markdown('<h1 style="text-align:center">Weather Visulization</h1>',unsafe_allow_html=True)

st.write("Write the name of the city and select the Temperature unit and Graph type")

city = st.text_input(label='NAME OF THE CITY/ STATE/ COUNTRY:')
city = city.title()

temp_unit = st.selectbox(label='Select Temperature unit',options=['Celcius','Farenheit','Kelvin'])

graph = st.selectbox(label='Select Graph type',options=['Line Chart','Bar Graph','Scatter Plot'])

submit = st.button(label='SUBMIT')

if city==None:
    st.error("Input a City!")

def get_coordinates(location):
    geolocator = Nominatim(user_agent="MyGeocoderApp/1.0")

    location = location.lower()

    location_info = geolocator.geocode(location)

    if location_info:
        return str(location_info.latitude), str(location_info.longitude)
    else:
        st.error("Location not found")

if submit:
    lat,lng = get_coordinates(city)

    url = "https://ai-weather-by-meteosource.p.rapidapi.com/hourly"

    querystring = {"lat":lat,"lon":lng,"timezone":"auto","language":"en","units":"auto"}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()

    time = []
    temp = []
    summary = []
    wind_speed = []
    cloud_cover = []
    humidity = []

    for i in range(len(response['hourly']['data'])):
        cur_time = response['hourly']['data'][i]['date']
        cur_temp = response['hourly']['data'][i]['temperature']
        speed = response['hourly']['data'][i]['wind']['speed']
        cloud = response['hourly']['data'][i]['cloud_cover']
        humid = response['hourly']['data'][i]['humidity']
        weather = response['hourly']['data'][i]['summary']

        time.append(cur_time)
        temp.append(cur_temp)
        wind_speed.append(speed)
        cloud_cover.append(cloud)
        humidity.append(humid)
        summary.append(weather)

    data = {'time':time,
    'temp(C)':temp,
    'wind speed':wind_speed,
    'cloud cover':cloud_cover,
    'humidity':humidity,
    'summary':summary}

    df = pd.DataFrame(data)

    today = datetime.now().date().isoformat()

    df = df[df['time'].str.find(today)==0]

    df.loc[:,'time'] = df.loc[:,'time'].replace(today+'T','',regex=True)

    df.loc[:,'temp(F)'] = df.loc[:,'temp(C)'].apply(lambda x: 32+((9/5)*x))

    df.loc[:,'temp(K)'] = df.loc[:,'temp(C)'].apply(lambda x: 273+x)

    plt.style.use('dark_background')

    if temp_unit=='Celcius':
        if graph=='Line Chart':

            st.markdown('<h3 style="text-align:center">Line Chart of Temperature (°C)</h3>',unsafe_allow_html=True)

            fig = px.line(data_frame=df,x=df['time'],y=df['temp(C)'],markers=True,labels={'time':'Time','temp(C)':'Temp'})
            fig.update_layout(xaxis=dict(tickangle=45), xaxis_title='Time', yaxis_title = 'Temperature (°C)')

            st.write(fig)
        elif graph=='Bar Graph':
            fig=plt.figure()

            st.markdown('<h3 style="text-align:center">Bar Graph of Temperature (°C)</h3>',unsafe_allow_html=True)

            plt.bar(df['time'],df['temp(C)'],color='orange')
            plt.xticks(rotation=45)

            st.write(fig)
        elif graph=='Scatter Plot':
            fig=plt.figure()

            st.markdown('<h3 style="text-align:center">Scatter Plot of Temperature (°C)</h3>',unsafe_allow_html=True)

            plt.scatter(df['time'],df['temp(C)'],c='yellow')
            plt.xticks(rotation=45)

            st.write(fig)
    
    elif temp_unit=='Farenheit':
        if graph=='Line Chart':

            st.markdown('<h3 style="text-align:center">Line Chart of Temperature (F)</h3>',unsafe_allow_html=True)

            fig = px.line(data_frame=df,x=df['time'],y=df['temp(F)'],markers=True,labels={'time':'Time','temp(F)':'Temp'})
            fig.update_layout(xaxis=dict(tickangle=45), xaxis_title='Time', yaxis_title = 'Temperature (F)')

            st.write(fig)
        elif graph=='Bar Graph':
            fig=plt.figure()

            st.markdown('<h3 style="text-align:center">Bar Graph of Temperature (F)</h3>',unsafe_allow_html=True)

            plt.bar(df['time'],df['temp(F)'],color='orange')
            plt.xticks(rotation=45)

            st.write(fig)
        elif graph=='Scatter Plot':
            fig=plt.figure()

            st.markdown('<h3 style="text-align:center">Scatter Plot of Temperature (F)</h3>',unsafe_allow_html=True)

            plt.scatter(df['time'],df['temp(F)'],c='yellow')
            plt.xticks(rotation=45)

            st.write(fig)
    
    elif temp_unit=='Kelvin':
        if graph=='Line Chart':
        
            st.markdown('<h3 style="text-align:center">Line Chart of Temperature(K)</h3>',unsafe_allow_html=True)

            fig = px.line(data_frame=df,x=df['time'],y=df['temp(K)'],markers=True,labels={'time':'Time','temp(K)':'Temp'},color_continuous_scale='Jet')
            fig.update_layout(xaxis=dict(tickangle=45), xaxis_title='Time', yaxis_title = 'Temperature (K)')

            st.write(fig)
        elif graph=='Bar Graph':
            fig=plt.figure()

            st.markdown('<h3 style="text-align:center">Bar Graph of Temperature (K)</h3>',unsafe_allow_html=True)

            plt.bar(df['time'],df['temp(K)'],color='orange')
            plt.xticks(rotation=45)

            st.write(fig)
        elif graph=='Scatter Plot':
            fig=plt.figure()

            st.markdown('<h3 style="text-align:center">Scatter Plot of Temperature (K)</h3>',unsafe_allow_html=True)

            plt.scatter(df['time'],df['temp(K)'],c='yellow')
            plt.xticks(rotation=45)

            st.write(fig)

    st.write('<br />',unsafe_allow_html=True)
    
    st.write('<h2>Impeding Temperature Changes : </h2>',unsafe_allow_html=True)
    st.write(f'<h5>{df['summary'].mode()[0]}!</h5>',unsafe_allow_html=True)

    st.write('<h2>Cloud coverage and Wind Speed</h2>',unsafe_allow_html=True)
    st.write(f'<h5>The current cloud coverage for {city} is </h5>',unsafe_allow_html=True)
    st.text(f'{format(df['cloud cover'].mean(),'.2f')} %')
    st.write(f'<h5>The current wind speed for {city} is </h5>',unsafe_allow_html=True)
    st.text(f'{format(df['wind speed'].mean(),'.2f')} m/s')