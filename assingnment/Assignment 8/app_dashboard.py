# Task 4: Mini Dashboard (app dashboard.
# Create a small dashboard with:
# 1. Title + Description
# "Simple Sales Dashboard"
# 2. A selectbox with months:
# months = ("January", "February". "March", "A
# 3. A static dictionary of monthly sales:
# sales = {
# "January": 1200.
# "February": 1500.
# "March": 900
# "April": 2000
# 4. Display selected month's sales using: st.metric() OR st write() 
# 5. Display a bar chart using st.bar_chart(list(sales values()))

import streamlit as st

st.title("Simple Sales Dashboard")
st.write("Sales according to months ")

sales={"January":1200,
       "February":1500,
       "March":900,
       "April":2000}

month=st.selectbox("Select Month",sales.keys())

st.metric("Sales",sales[month])

st.bar_chart(list(sales.values()))
