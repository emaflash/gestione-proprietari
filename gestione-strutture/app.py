import streamlit as st
from utils.db_utils import init_db
from utils.auth import login

st.set_page_config(page_title="Gestione Strutture", layout="wide")

init_db()

st.title("🏨 Gestione Strutture Ricettive")

if login():
    st.sidebar.markdown("### Navigazione")
    st.sidebar.markdown("Usa il menu laterale per accedere alle sezioni:")
    st.sidebar.write("🏠 Dashboard\n👤 Proprietari\n🏡 Immobili\n💬 Comunicazioni")
