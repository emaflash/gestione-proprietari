import streamlit_authenticator as stauth
import streamlit as st

def login():
    names = ["Emanuele", "Team"]
    usernames = ["ema", "team"]
    passwords = stauth.Hasher(["1234", "abcd"]).generate()

    authenticator = stauth.Authenticate(
        names, usernames, passwords, "cookie_gestione", "chiavefirma", cookie_expiry_days=30
    )

    name, auth_status, username = authenticator.login("Login", "main")

    if auth_status:
        authenticator.logout("Logout", "sidebar")
        st.sidebar.success(f"Benvenuto {name}")
        return True
    elif auth_status is False:
        st.error("Credenziali non valide")
    return False
