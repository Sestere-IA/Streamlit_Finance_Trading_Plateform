#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import datetime
import pandas as pd
import numpy as np


st.title("Application Streamlit version 1 - Entrée csv, Sortie dashboard")


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache #### Role de st.cache


def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data



# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')


# Load 10,000 rows of data into the dataframe. #### Utilisation de la fonction load_data: Chargement de 10000 lignes
data = load_data(10000)


# Notify the reader that the data was successfully loaded.
data_load_state.text('Done! (using st.cache)')


###st.subheader('Raw data')
###st.write(data) #### Récupération du tableau

if st.checkbox('Show raw data'): #### Si la checkbox est cochée
    st.subheader('Raw data') #### Affichage du texte
    st.write(data) #### Afficher les données associées


st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]  #### COnstruction de l'histogramme


st.bar_chart(hist_values) #### Affichage de l'histogramme


st.subheader('Map of all pickups')
st.map(data) #### Carte des prises de clients par les chauffeurs ubers

#hour_to_filter = 17  #### Afficher une carte des véhicules présents sur la ville de NY

#hour_to_filter = st.number_input("Heure", min_value=0, max_value=23, step=1)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h

filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter] #### Filtrer les données sur l'heure choisie
st.subheader(f'Map of all pickups at {hour_to_filter}:00') #### Sous titre de la map à l'heure choisie
st.map(filtered_data) #### Affichage des courses à 17h00 sur la ville de NY



# In[ ]:




