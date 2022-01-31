import streamlit as st
from database import bdd_setting
import pandas as pd


def app():
    st.title("Liste d'utilisateurs et historiques des transactions")
    st.write("Historique des transactions passées")
    result = bdd_setting.see_bdd_actions()
    df = pd.DataFrame(result, columns=["index", "Username", "Date", "Action", "Quantity", "Total Transaction", "Indicator"])
    st.table(df)
