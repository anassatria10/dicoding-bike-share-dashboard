### LIBRARY ###

import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import plotly.express as px
import streamlit as st

### SETTING LAYOUT ###

st.set_page_config(
    page_title='Bike Share Dashboard',
    layout='wide'
)

### LOAD DATA ###

def load_data():
    data = pd.read_csv('./data/hour.csv')
    return data

data = load_data()

### PREPROCESSING ###

def prepocessing(dataframe):
  dataframe['dteday'] = pd.to_datetime(dataframe['dteday'])
  
  dataframe['month'] = dataframe['dteday'].dt.month_name()
  dataframe['day'] = dataframe['dteday'].dt.day_name()
  
  dataframe['season'] = dataframe['season'].replace([1, 2, 3, 4], ['Springer', 'Summer', 'Fall', 'Winter'])
  dataframe['yr'] = dataframe['yr'].replace([0, 1], [2011, 2012])
  dataframe['workingday'] = dataframe['workingday'].replace([0, 1],['No', 'Yes'])
  dataframe['weathersit'] = dataframe['weathersit'].replace([1, 2, 3, 4], ['Clear', 'Mist + Cloudy', 'Light Snow', 'Heavy Rain + Ice Pallets'])
  dataframe['temp'] = dataframe['temp']*41
  dataframe['atemp'] = dataframe['atemp']*50
  dataframe['hum'] = dataframe['hum']*100
  dataframe['windspeed'] = dataframe['windspeed']*67
  
  return dataframe

df = prepocessing(data)

### DATAFRAME FUNCTION ###

def create_daily_bike_share(df):
    daily_riders_df = df.resample(rule='D', on='dteday').agg({
        'casual': 'sum',
        'registered': 'sum', 
        'cnt': 'sum'
    })
    
    daily_riders_df = daily_riders_df.reset_index()
    
    return daily_riders_df

def create_monthly_bike_share(df):
    month_order = df['month'].unique().tolist()
    bike_share_monthly = df.groupby('month').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    })
    
    bike_share_monthly = bike_share_monthly.reindex(month_order).reset_index()

    return bike_share_monthly

def create_bike_share_days(df):
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    bike_share_days = df.groupby('day').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    })
    
    bike_share_days = bike_share_days.reindex(day_order).reset_index()
    
    return bike_share_days

def create_hourly_bike_share(df):
    hourly_bike_share = df.groupby('hr').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    })
    
    hourly_bike_share = hourly_bike_share.reset_index()
    
    return hourly_bike_share

def create_bike_share_season_and_weather(df):
    season_by_weather = df.groupby(['season', 'weathersit']).agg({
        'casual': 'sum', 
        'registered': 'sum',
        'cnt': 'sum'
    })
    
    season_by_weather = season_by_weather.reset_index()
    
    return season_by_weather

### FILTER ###

min_date = df['dteday'].min()
max_date = df['dteday'].max()

### SIDEBAR ###

with st.sidebar:
    # add the image 
    st.image('./asset/hours.png')
    
    start_date, end_date = st.date_input(
        label='Datetime :',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

### DEFINE MAIN DATAFRAME ###

df = df[(df['dteday'] >= str(start_date))
        & (df['dteday'] <= str(end_date))]

daily_df = create_daily_bike_share(df)
monthly_df = create_monthly_bike_share(df)
days_of_df = create_bike_share_days(df)
hourly_df = create_hourly_bike_share(df)
season_by_weather_df = create_bike_share_season_and_weather(df)

#### MAIN PAGE ###

st.title('Bike Share Dashboard:bicyclist:')

metric1, metric2, metric3 = st.columns(3)

with metric1:
    with st.container(border=True):
        total_riders = df['cnt'].sum()
        st.metric(label='Total Number of Bike Share :', value=total_riders)
    
with metric2:
    with st.container(border=True):
        total_registered = df['registered'].sum()
        st.metric(label='Total Registered :', value=total_registered)
    
with metric3:
    with st.container(border=True):
        total_casual = df['casual'].sum()
        st.metric(label='Total Casual :', value=total_casual)

### Visualization 1 ###

with st.container(border=True):
    chart1 = px.area(daily_df, x='dteday', y=['casual', 'registered','cnt'], labels={'variable': 'user', 'dteday': 'datetime', 'value': 'total'})
    chart1.update_layout(
        title={
            'text': 'Bike Share Trend of Users',
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title='datetime',
        yaxis_title='total',
        legend_traceorder='reversed',
        hovermode='x unified'
    )
    
    st.plotly_chart(chart1)

### Visualization 2 ###

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        monthly_order = monthly_df['month'].unique().tolist()
        chart2 = px.bar(monthly_df, x=['casual', 'registered'], y='month', category_orders={'month': monthly_order}, labels={'variable': 'user', 'value': 'total'}, text_auto=True)
        chart2.update_layout(
            title={
                'text': 'Monthly Trend of Users',
                'x': 0.55,
                'xanchor': 'center'
            },
            legend={
                'orientation': 'h',
                'x': 0.5,
                'y': 1.09,
                'xanchor': 'center'
            },
            legend_title=None,
            xaxis_title='total'
        )
        st.plotly_chart(chart2)

with col2:
    with st.container(border=True):
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        chart3 = px.bar(days_of_df, x=['casual', 'registered'], y='day', category_orders={'day': day_order}, labels={'variable': 'user', 'value': 'total'}, text_auto=True)
        chart3.update_layout(
            title={
                'text': 'Day of the week Trend of Users',
                'x': 0.55,
                'xanchor': 'center'
            },
            legend={
                'orientation': 'h',
                'x': 0.5,
                'y': 1.09,
                'xanchor': 'center'
            },
            legend_title=None,
            xaxis_title='total'
        )
        st.plotly_chart(chart3)
        
### Visualization 3 ###

with st.container(border=True):
    chart4 = px.line(hourly_df, x='hr', y=['casual', 'registered'], labels={'variable': 'user', 'hr': 'hour', 'value': 'total'}, markers=True)
    chart4.update_layout(
        title={
            'text': 'Hourly Trend of Users',
            'x': 0.47,
            'xanchor': 'center'
        },
        xaxis_title='hour',
        yaxis_title='total',
        legend_traceorder='reversed',
        hovermode='x unified'
    )
    st.plotly_chart(chart4)

### Visualization 4 ###

with st.container(border=True):
    chart5 = px.bar(season_by_weather_df, x='weathersit', y=['casual','registered'], facet_col='season', category_orders={'weathersit': ['Clear', 'Mist + Cloudy', 'Light Snow', 'Heavy Rain + Ice Pallets']}, labels={'variable': 'user', 'value': 'total'}, barmode='group', text_auto=True)
    chart5.update_traces(textposition='outside')
    chart5.update_layout(
        title={
            'text': 'Season Trend of Users',
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title='weathersit',
        yaxis_title='total',
        legend_traceorder='reversed',
    )
    
    st.plotly_chart(chart5)