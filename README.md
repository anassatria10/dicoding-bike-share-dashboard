# Bike Share Dashboard

## Description 
This project aims to tackle business challenges by developing an interactive dashboard that analyzes data and presents it visually to uncover valuable insights.

The interactive dashboard can be acess on this link : https://dicoding-bike-share-dashboard.streamlit.app/

## Defining Business Questions
1. When are the busy and quite times of year for bike sharing used?
2. What is the overall trend of bike users throughout the year?
3. How does bike user differ between weekdays and weekends?
4. What is the hourly trend of users during the bike share operation?
5. How does weather condition impact the usage the bike-sharing accross different season?

## Insights and Findings
1. The busiest time in 2011 was on July 4th, with 6.043 users, while the lowest number of users, 431, occurred on January 27th. In the following year, the number of bicycle users in increased, reaching 8,714 on September 15, 2012, while the lowest total bike sharing users was only 22 on October 29, 2012.

2. The chart shows a significant increase in total number of users from January to July, peaking in July with 78.157k for casual users. Unlike casual users, registered users reached the highest peak in August, at around 279.155k. After that, the number of users gradually declined until the end of the year.

3. Weekdays (Monday-Friday) show higher registered user activity, with the peak occurring on Thursday. bikes are more likely to be used by registered users for commuting during weekdays. Weekends (Saturday and Sunday) show significantly higher casual user activity, with Saturday reaching 153.853k casual users, the highest among all days. casual users primarily use bikes for leisure or recreational purposes on weekends.

4. Registered : The trend of bicycle use among registered users is more active in the morning (starting activities) and afternoon (estimated activities have ended). The increase occurs starting at 5 and at 8 is the ideal time for registered users to start activities. Then, during the day it starts to decline. In fact, in the afternoon the number of users is higher than in the morning. The total number of registered users is 37,400 higher than in the morning.
Casual : Casual user trends are more stable, occurring between 13-17 hours, ranging from 50,000 to 55,000 users. Casual user activities are more frequent during the day after experiencing a positive trend in the morning and starting to decline after 17:00.

5. Casual users are highly weather-sensitive, showing a sharp decline in adverse conditions like snow or heavy rain. Registered users are less affected by weather changes but still exhibit reduced activity in harsh conditions. Clear weather is the most favourable for both user groups, especially in Fall and Summer.

## Dataset 

Bike Sharing Dataset : https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset

Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions, precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA

## Setup Environment
```
mkdir dicoding-bike-share-dashboard
cd dicoding-bike-share-dashboard
pip install virtualenv
python -m venv .env
.\.env\Scripts\activate
pip install -r requirements.txt
```

## Run Streamlit App
```
cd dashboard
streamlit run app.py
```
