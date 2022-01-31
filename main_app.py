import streamlit as st
from pages import connection, homepage, create_users, list_users
from multiapp import MultiApp

app = MultiApp()

if 'pseudo' not in st.session_state:
    connection_name = "Connection"
else:
    connection_name = st.session_state["pseudo"]

app.add_app("Home page", homepage.app)
app.add_app(connection_name, connection.app)
app.add_app("Liste d'actions utilisateurs", list_users.app)
app.add_app("Create Account", create_users.app)

app.run()
