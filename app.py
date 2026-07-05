app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi dashboard agar lebar (lebar penuh)
st.set_page_config(layout="wide", page_title="Expenses Dashboard")

st.title("📊 coba-coba")

# Simulasi data
data = {
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Amount': [5000, 2000, 8000, 3000, 4500, 1500],
    'Category': ['Hardware', 'Software', 'Travel', 'Hardware', 'Marketing', 'Office'],
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar']
}
df = pd.DataFrame(data)

# Sidebar Filter
dept = st.sidebar.multiselect("Pilih Departemen:", df['Department'].unique())
if dept:
    df = df[df['Department'].isin(dept)]

# Kartu KPI (Bagian atas)
col1, col2, col3 = st.columns(3)
col1.metric("Total Expenses", f"INR {df['Amount'].sum():,}")
col2.metric("Average Expense", f"INR {df['Amount'].mean():,.0f}")
col3.metric("Total Transactions", len(df))

# Grafik (Bagian bawah)
c1, c2 = st.columns(2)
with c1:
    fig1 = px.bar(df, x='Department', y='Amount', title="Expenses by Dept", color='Department')
    st.plotly_chart(fig1, use_container_width=True)
with c2:
    fig2 = px.pie(df, values='Amount', names='Category', title="Expenses by Category")
    st.plotly_chart(fig2, use_container_width=True)

st.dataframe(df, use_container_width=True)
