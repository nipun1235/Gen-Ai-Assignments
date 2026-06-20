# Task 3: Product Form
# Create a simple form UI
# 1. Use Streamlit sidebar to enter:
# Product name
# Category(selectbox with 3-5 options)
# Price
# 2. When user clicks "Add Product",show:
# A Success message
# The Product deatils in a clean format

import streamlit as st

Product_name=st.sidebar.text_input("Enter Product Name ")

Category=st.sidebar.selectbox("Category",["Electronics","Accessories","Dairy Product","Audio","PS 5 Games"])

price=st.sidebar.number_input("Enter the Product Amount ")

if st.sidebar.button("Add Product"):
    st.write("Product Added Successfully !")

    st.table({"Product Name": [Product_name],
              "Category": [Category],
              "Price": [price]})