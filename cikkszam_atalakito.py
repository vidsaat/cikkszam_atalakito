import streamlit as st
import pandas as pd
import re
from io import StringIO

st.title("Cikkszám átalakító")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, header=None)

    dataframe["cikkszam"] = dataframe[0].apply(lambda x: re.sub(r"[^0-9]", "", x))
    st.dataframe(dataframe)

    st.download_button(
        "letoltes",
        dataframe.to_csv(index=False).encode("utf-8"),
        "cikkszam_szamkent.csv",
        "text/csv",
        key="download-csv",
    )
