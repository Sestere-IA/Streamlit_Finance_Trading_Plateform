import streamlit as st
from database import bdd_setting
from datetime import date
import os
import hashlib



def app():
    if "pseudo" not in st.session_state:
        st.title("Création de compte")
        st.write("Renseignez vos informations afin de vous créer un compte")
        user_name = st.text_input("Name", placeholder="Your Name")
        user_surname = st.text_input("Surname", placeholder="Your Surname")
        user_capital = st.number_input("Capitale", step=100, min_value=100)
        user_username = st.text_input("Username", placeholder="Your Username")
        user_password = st.text_input("Password", placeholder="Your Password", type="password")
        user_password_repeate = st.text_input("Password Repeate", type="password", placeholder="Repeate your Password")

        def create_user():
            today = date.today()
            salt = os.urandom(32)
            hashed_passwords = hashlib.pbkdf2_hmac('sha256', user_password.encode('utf-8'), salt, 100000)
            storage_password = salt + hashed_passwords
            bdd_setting.insert_client_in_bdd(user_username, storage_password,
                                             int(user_capital), 0, user_name, user_surname,
                                             today.strftime('%Y-%m-%d %H:%M:%S'))
            st.success("You have successfully created a valid Account")

        if st.button("Signup"):
            if user_name != "" and user_surname != "" and user_username != "" and user_password != "":
                if user_password == user_password_repeate:
                    if bdd_setting.check_identifiant_exist():
                        for username in bdd_setting.check_identifiant_exist():
                            if username[0] == user_username:
                                st.error("Username already taken, try with other username")
                            else:
                                create_user()
                    else:
                        create_user()

                else:
                    st.error("Repeate password is not the same")
            else:
                st.error("Please, fill all components")
    else:
        st.title("Bonjour " + st.session_state["pseudo"])
        st.write("Vous ête actuellement deja connecté à un compte")
        if st.button("Se déconnecter"):
            del st.session_state['pseudo']
            st.success("Vous ête maintenant déconnecté")

