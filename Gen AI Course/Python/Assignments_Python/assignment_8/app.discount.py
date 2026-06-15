'''
Task 2: Price Calculator (app_discount.py)
Build a simple price calculator app that:
1. Takes product price (number input)
2. Takes discount percentage (slider from 0 to 50%)
3. On button click, calculates discounted price
4. Shows result using st.success()
Example:
Original Price: 1000
Discount: 10%
Final Price: 900
Extra (optional): Show comparison in a small table:
Before | After
(Use st.table() with a simple list of lists.)
'''
import streamlit as st

price=st.number_input("Enter the price")

disc=st.slider("Discount Percentage",0, 50, 0)

if st.button("calculate"):
    new_price= price -(price * disc/100)
    data=[
        ["original price", f"{price}"],
        ["Discounted Price", f"{new_price}"]
    ]
    st.table(data)