import streamlit as st
import pandas as pd
import requests

st.title("📊 NEPSE Dashboard")

url = "https://www.nepalstock.com/api/nots/securityDailyTradeStat/58"
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
data = res.json()

df = pd.DataFrame(data)

st.dataframe(df.head(20))
