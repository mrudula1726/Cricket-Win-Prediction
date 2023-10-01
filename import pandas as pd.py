import pandas as pd
import streamlit as st
import pickle

from pandas import DataFrame

team1 = ['Australia', 'Pakistan', 'England', 'South Africa', 'India',
         'New Zealand', 'Sri Lanka', 'Bangladesh', 'West Indies',
         'Afghanistan', 'Zimbabwe', 'Scotland', 'Netherlands', 'Kenya']
team2 = ['West Indies', 'England', 'Pakistan', 'New Zealand', 'Bangladesh',
         'Australia', 'India', 'Afghanistan', 'South Africa', 'Sri Lanka',
         'Ireland', 'Kenya', 'Netherlands', 'Zimbabwe', 'Scotland']
ground = ['England', 'India', 'Australia', 'Scotland', 'Antigua',
          'Sri Lanka', 'South Africa', 'New Zealand', 'Bangladesh', 'Qatar',
          'Pakistan', 'Saint Lucia', 'Dominica', 'Netherlands',
          'Island of Barbados', 'Ireland', 'Jamaica', 'Kenya', 'Guyana',
          'Zimbabwe', 'United Arab Emirates', 'West Indies', 'St.Kitts',
          'Oman', 'United States of America', 'Tarouba', 'Namibia', 'Nepal']
format = ['ODI', 'T20I', 'Test']
toss = ['lost', 'won']
bat = [1, 2]
venue = ['Home', 'Neutral', 'Away']
pipe = pickle.load(open('pipe.pkl', 'rb'))
st.title('Cricket Outcome Predictor')
col1, col2, col3 = st.columns(3)

with col1:
    Team1 = st.selectbox('Select team1', sorted(team1))
with col2:
    Team2 = st.selectbox('Select team2', sorted(team2))
with col3:
    Ground_Country = st.selectbox('Select ground country', sorted(ground))

Venue = st.selectbox('Select venue for team1', sorted(venue))
Format = st.selectbox('Select Format of the cricket match', sorted(format))
col4, col5 = st.columns(2)
with col4:
    Toss_by_Team1 = st.selectbox('Team1 won or lost the toss', sorted(toss))
with col5:
    Bat_by_Team1 = st.selectbox('Team1 batted 1st or 2nd', sorted(bat))

if st.button('Predict winning probability'):
    input_df = pd.DataFrame({'Team1': [Team1], 'Team2': [Team2], 'Ground_Country': [Ground_Country],
                       'Venue': [Venue], 'Format': [Format], 'Toss_by_Team1': [Toss_by_Team1],
                       'Bat_by_Team1': [Bat_by_Team1]})
result = pipe.predict_proba(input_df)
loss = result[0][0]
tie = result[0][1]
win = result[0][2]
# st.text(result)
st.header(Team1 + "- " + str(round(win * 100)) + "%")
st.header(Team2 + "- " + str(round(loss * 100)) + "%")
st.header("Tie - {:.2f}%".format(tie*100))
