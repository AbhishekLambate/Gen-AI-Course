'''
Task 4: Mini Dashboard (app_dashboard.py)
Create a small dashboard with:
1. Title + Description "Simple Sales Dashboard"
2. A selectbox with months: months = ["January", "February", "March", "April"]
3. A static dictionary of monthly sales:
sales = {
"January": 1200,
"February": 1500,
"March": 900,
"April": 2000
}
4. Display selected month's sales using: st.metric() OR st.write()
5. Display a bar chart using: st.bar_chart(list(sales.values())) (No pandas required - simple list is allowed.)
'''

import streamlit as st
st.title("Simple Sales Dashboard")
st.text("This is a simple sales dashboard build using streamlit library of python.")

months = ["January", "February", "March", "April"]
selected_month = st.selectbox("Select a month:", months)

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}
st.metric(label=f"Sales for {selected_month}", value=sales[selected_month])

st.bar_chart(list(sales.values()))