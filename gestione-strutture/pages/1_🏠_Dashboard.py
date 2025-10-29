import streamlit as st
from utils.db_utils import get_df

st.title("📊 Dashboard")

n_prop = get_df("SELECT COUNT(*) AS n FROM proprietari")["n"][0]
n_imm = get_df("SELECT COUNT(*) AS n FROM immobili")["n"][0]

st.metric("Proprietari", n_prop)
st.metric("Immobili", n_imm)
