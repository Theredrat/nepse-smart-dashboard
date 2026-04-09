import streamlit as st
import pandas as pd

st.title("NEPSE Dashboard Working ✅")

data = {
"Stock": ["NABIL", "NTC", "HIDCL"],
"Price": [800, 900, 200]
}

df = pd.DataFrame(data)

st.dataframe(df)
