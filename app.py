import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Game Sales Analysis", page_icon=":moon:", layout="wide")
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie = load_lottie('https://assets3.lottiefiles.com/packages/lf20_49rdyysj.json')


with st.container():
    st.subheader('Hey, I am Ashmit Mahindroo studying in Class 8th :wave:')
    st.write('---')
    left_column, right_column = st.columns(2)

    with left_column:
        st.title("This is the Data Analysis on Game Sales")
    with right_column:
        st_lottie(lottie, height=140)

with st.container():
    data = pd.read_csv("./game_sales.csv")
    st.header("This is all the Game Sales Data")
    st.dataframe(data, hide_index=True)
    # max_occurrence = data["Publisher"].value_counts().idxmax()
    st.subheader("Insights of top 10 games")
    st.markdown("<ul><b><li>Wii Sports has been the most selling game(82.24 Million global sales).</li><li>Most published games of top 10 are on Wii Sports platform(5 games).</li><li> All of the games in top 10 are published on Nintendo.</li></b></ul>", True)
    st.write('---')

with st.container():
    st.header("Sales by Genre")
    region_options = ['Global', 'North America', 'Europe', 'Japan', 'Others']
    
    selected_region = st.selectbox('Select a region', region_options, key='region_dropdown')
    
    column_mapping = {
        'Global': 'Global_Sales',
        'North America': 'NA_Sales',
        'Europe': 'EU_Sales',
        'Japan': 'JP_Sales',
        'Others': 'Other_Sales'
    }
    
    filtered_data = data[['Genre', column_mapping[selected_region]]]
    
    genre_sales = filtered_data.groupby('Genre')[column_mapping[selected_region]].sum().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(genre_sales['Genre'], genre_sales[column_mapping[selected_region]])
    ax.set_xlabel('Genre')
    ax.set_ylabel('Sales (in millions)')
    ax.set_title(f'Sales by Genre in {selected_region}')
    
    plt.xticks(rotation=90)
    st.pyplot(fig)
    
    st.subheader("Insights of Sales by Genre in Global, Europe, North America and Other regions")
    st.markdown("<ul><b><li>Actions games are the highest sold games followed up by Sports and Shooter games.</li><li>Strategy games are the least sold games.</li></b></ul>", True)
    
    st.subheader("Insights of Sales by Genre in Japan Region")
    st.markdown("<ul><b><li>Role playing games are the highest sold games followed up by Actions and Platform games</li><li>Shooter games are the least sold games.</li></b></ul>",True)

    st.subheader("Key Insight")
    st.markdown("<ul><b><li>Action games are in the top 3 most selling games of all regions.</li></b></ul>", True)
    st.write('---')

with st.container():
    st.header("Sales by Year")
    selected_region = st.selectbox('Select a region', list(column_mapping.keys()), key='yregion_dropdown')
    filtered_data = data[['Year', column_mapping[selected_region]]]
    sales_by_year = filtered_data.groupby('Year')[column_mapping[selected_region]].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(sales_by_year['Year'], sales_by_year[column_mapping[selected_region]])
    ax.set_xlabel('Year')
    ax.set_ylabel('Sales (in millions)')
    ax.set_title(f'Sales by Year - {selected_region}')
    st.pyplot(fig)
    st.subheader("Insights of Sales by Year")
    st.markdown("<ul><b><li>2008 has been the most selling year followed</li><li>Almost No sales has been made in years 2017-2020.</b></ul>", True)
    st.write('---')

with st.container():
    st.header("Sales by Platform")
    selected_region = st.selectbox('Select a region', list(column_mapping.keys()), key='pregion_dropdown')
    filtered_data = data[['Platform', column_mapping[selected_region]]]
    sales_by_platform = filtered_data.groupby('Platform')[column_mapping[selected_region]].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(sales_by_platform['Platform'],sales_by_platform[column_mapping[selected_region]],)
    ax.set_xlabel('Sales (in millions)')
    ax.set_ylabel('Platform')
    ax.set_title(f'Sales by Platform - {selected_region}')
    st.pyplot(fig)
    st.subheader("Insights of Sales by Platform")
    st.markdown("<ul><b><li>Platforms such as X360, PS2, PS3 and SNES has been very highselling platforms</li><li>Platforms such as WS, TG16 and 3DO has been very low selling platforms</li></b></ul>", True)
    st.subheader("Key Insight")
    st.markdown("<ul><b><li>In Sales by Platform, each region has been very unique in its sales</li></b></ul>",True)
    st.write('---')

with st.container():
    st.header("Additional Insights")
    st.markdown("<ul><b><li>Publisher with the most games is Electronic Arts</li><li>Publisher with the least games: Headup Games</li><li>Platform with the most games is DS</li><li> Platform with the least games is GG</li></b></ul>",True)

    st.header("Overall Insights")
    st.markdown("<ul><b><li>Japan Sales in every aspect has been quite different from other regions</li><li>More Actions games need to be published more and strategy games need to be published less in order to increase the game sales</li><li>Unless a miracle happens, Games has been a dying market for the last few years</li></b></ul>",True)

