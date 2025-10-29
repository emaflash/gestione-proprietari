import streamlit as st
from utils.db_utils import get_df, execute
from datetime import date

st.title("💬 Comunicazioni")

df = get_df("""
SELECT c.data, p.nome AS proprietario, c.canale, c.messaggio
FROM comunicazioni c
LEFT JOIN proprietari p ON c.proprietario_id = p.id
ORDER BY c.data DESC
""")
st.dataframe(df)

st.subheader("➕ Registra Comunicazione")
proprietari = get_df("SELECT id, nome FROM proprietari")
scelta = st.selectbox("Proprietario", proprietari["nome"]) if not proprietari.empty else None
data = st.date_input("Data", date.today())
canale = st.selectbox("Canale", ["Email", "Telefono", "WhatsApp", "Altro"])
messaggio = st.text_area("Messaggio")

if st.button("Salva"):
    id_prop = proprietari.loc[proprietari["nome"] == scelta, "id"].values[0]
    execute(
        "INSERT INTO comunicazioni (proprietario_id, data, canale, messaggio) VALUES (?, ?, ?, ?)",
        (id_prop, str(data), canale, messaggio),
    )
    st.success("Comunicazione registrata!")
    st.rerun()
