
import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

st.set_page_config(page_title="Power BI Style Dashboard", layout="wide")
st.title("📊 Ultra-Polished Sales Dashboard")

uploaded_file = st.file_uploader("Upload CSV/Excel with columns: Date, Product, Sales", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    else:
        df = pd.read_excel(uploaded_file, parse_dates=["Date"])

    st.write("Dashboard will be here!")
else:
    st.warning("⬆️ Please upload a CSV or Excel file with columns: Date, Product, Sales")
