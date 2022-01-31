import streamlit as st
from database import bdd_setting
import hashlib


def app():
    if 'pseudo' not in st.session_state:
        st.title("Connexion à son compte")
        st.write("Renseignez votre pseudo et votre mot de passe pour vous connecter")
        user_username = st.text_input("Username", placeholder="Your Username")
        user_password = st.text_input("Password", placeholder="Your Password", type="password")

        if st.button("Signin"):

            for username_password in bdd_setting.check_identififiant_password():
                salt_from_storage = username_password[1][:32]
                key_from_storage = username_password[1][32:]
                new_key = hashlib.pbkdf2_hmac(
                    'sha256',
                    user_password.encode('utf-8'),  # Convert the password to bytes
                    salt_from_storage,
                    100000
                )
                if user_username == username_password[0] and new_key == key_from_storage:
                    st.success("Vous ête maintenant connecté")
                    st.info("Go to Login Menu to login")

                    if 'pseudo' not in st.session_state:
                        st.session_state["pseudo"] = user_username

                else:
                    st.error("Username or password incorrect")
    else:
        st.title("Bonjour " + st.session_state["pseudo"])
        st.write("Voici vos informations")
        st.write("Blabla")
        if st.button("Se déconnecter"):
            del st.session_state['pseudo']
            st.success("Vous ête maintenant déconnecté")