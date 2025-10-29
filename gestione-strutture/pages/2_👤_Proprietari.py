import streamlit as st
from utils.db_utils import get_df, execute

st.title("👤 Gestione Proprietari")

df = get_df("SELECT * FROM proprietari")
st.dataframe(df)

st.subheader("➕ Aggiungi Proprietario")
nome = st.text_input("Nome")
email = st.text_input("Email")
telefono = st.text_input("Telefono")
note = st.text_area("Note")

if st.button("Salva"):
    execute("INSERT INTO proprietari (nome, email, telefono, note) VALUES (?, ?, ?, ?)", (nome, email, telefono, note))
    st.success("Proprietario aggiunto!")
    st.rerun()
