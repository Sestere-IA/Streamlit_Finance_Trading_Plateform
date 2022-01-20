#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import datetime

liste_choix = ["Bad", "Normal", "Good", "Good2", "Good3"]

st.title("Application Streamlit version 0")
st.write("Cette application est à adapter au problème de détection des jumeaux des entreprises")
user_id = st.text_input("ID", value="Your ID")

info = st.text_area("Share some information about you", "Put information here",
                    help='You can write about your hobbies or family')


age = st.number_input("Age", min_value=18, max_value=100, step=1)

birth_date = st.date_input("Date of Birth", min_value=datetime.date(1921, 1, 1),
                           max_value=datetime.date(2003, 12, 31))


smoke = st.checkbox("Do you smoke?")
genre = st.radio("Which movie genre do you like?",
                 options=['horror', 'adventure', 'romantic'])

weight = st.slider("Choose your weight", min_value=40., max_value=150., step=0.5)



physical_form = st.selectbox("Select level of your physical condition",
                             options=liste_choix)


colors = st.multiselect('What are your favorite colors',
                        options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])


image = st.file_uploader("Upload your photo", type=['jpg', 'png'])


submit = st.button("Submit") #### Affichage du Bouton

#### Effet du bouton 

if submit:
    st.write("You submitted the form")


click = st.sidebar.button('Click me!')
if click:
    st.sidebar.write("You clicked the button")


col1, col2 = st.beta_columns(2)
with col1:
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    st.button("Like cats")
with col2:
    st.image("https://static.streamlit.io/examples/dog.jpg", width=355)
    st.button("Like dogs")

# In[ ]:




