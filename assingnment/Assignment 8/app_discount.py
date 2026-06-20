# Task 2: Price Calculator
# Build a simple Price Calculator app that:
# Takes product price (number input)
# On button click,calculates discounted price
# Show result using st.success()


import streamlit as st

price=st.number_input("Enter Product Price: ",min_value=0)

discount=st.slider("Discount Percentage: ",0, 50)

if st.button("Calculate Discounted Price "):
    Final_price=price-(price*discount/100)

    st.success(f"Final Price ={Final_price}")
## Extra 
    st.table({
        "Before": [price],
        "After" : [Final_price]})