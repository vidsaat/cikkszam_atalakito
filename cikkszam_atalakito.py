import streamlit as st
import pandas as pd
import re

st.title("Cikkszám átalakító")
st.text_input("Kosár fájl:", key="filename")
file_path = st.session_state.filename
kosar = pd.read_csv(file_path, header=None, sep=";")
kosar["cikkszam"] = kosar[0].apply(lambda x: re.sub(r"[^0-9]", "", x))
new_filename = "cikkszam_szamkent_" + file_path
st.dataframe(kosar)
kosar.to_csv(new_filename)
