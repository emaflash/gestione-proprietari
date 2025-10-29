import streamlit as st
from utils.db_utils import get_df, execute

st.title("🏡 Gestione Immobili")

df = get_df("""
SELECT i.id, i.nome, i.indirizzo, i.capienza, p.nome AS proprietario
FROM immobili i
LEFT JOIN proprietari p ON i.proprietario_id = p.id
""")
st.dataframe(df)

st.subheader("➕ Aggiungi Immobile")

proprietari = get_df("SELECT id, nome FROM proprietari")
scelta = st.selectbox("Proprietario", proprietari["nome"]) if not proprietari.empty else None
nome = st.text_input("Nome immobile")
indirizzo = st.text_input("Indirizzo")
capienza = st.number_input("Capienza", 1, 50, 2)
licenza = st.text_input("Licenza")
note = st.text_area("Note")

if st.button("Salva"):
    id_prop = proprietari.loc[proprietari["nome"] == scelta, "id"].values[0]
    execute(
        "INSERT INTO immobili (proprietario_id, nome, indirizzo, capienza, licenza, note) VALUES (?, ?, ?, ?, ?, ?)",
        (id_prop, nome, indirizzo, capienza, licenza, note),
    )
    st.success("Immobile aggiunto!")
    st.rerun()
