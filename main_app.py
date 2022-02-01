import streamlit as st
from pages import connection, homepage, create_users, list_users
from multiapp import MultiApp
from database import bdd_setting


class Main:
    """
    Chargement de l'app
    """

    def __init__(self):
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


def print_hi(name):
    """
    Dire bonjour à l'utisateur qui utilisera ce script :D
    :param name:
    String
        Le nom de l'utilisateur
    """
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {}'.format(name))  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('BONJOUR :D')
    bdd_setting.test_con()
    Main()
