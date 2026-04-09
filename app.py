import streamlit as st
import pandas as pd
import requests

st.title("📊 NEPSE Dashboard")

def get_data():
try:
url = "https://www.nepalstock.com/api/nots/securityDailyTradeStat/58"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
data = res.json()
return pd.DataFrame(data)
except:
return pd.DataFrame()

df = get_data()

if df.empty:
st.write("❌ Data not loading")
else:
st.dataframe(df.head(20))
