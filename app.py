from db import init_db, add_expense, get_expenses, delete_expense
import streamlit as st
import pandas as pd

init_db()

st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title(" Expense Tracker")

with st.sidebar:
    st.header("Add expense")
    amount = st.number_input("Amount", min_value=0.01, step=0.50)
    category = st.selectbox("Category", ["Food", "Rent", "Transport", "Fun", "Other"])
    date = st.date_input("Date")
    note = st.text_input("Note")
    if st.button("Add"):
        add_expense(amount, category, str(date), note)
        st.success(f"Added ${amount:.2f} to {category}")
          

df= pd.DataFrame(get_expenses(), columns=['ID', 'Amount', 'Category', 'Date', 'Note'])


col1, col2, col3 = st.columns(3)
col1.metric("Total this month", "$0.00")
col2.metric("Top category", "-")
col3.metric("Daily average", "$0.00")

st.dataframe(df)