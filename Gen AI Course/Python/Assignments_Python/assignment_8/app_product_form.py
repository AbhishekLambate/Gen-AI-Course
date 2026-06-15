'''
Task 3: Product Form (app_product_form.py)
Create a simple form UI:
1. Use Streamlit sidebar to enter:
o Product Name
o Category (selectbox with 3-5 options)
o Price
2. When user clicks "Add Product", show:
o A success message
o The product details in a clean format
Use components:
st.sidebar.text_input
st.sidebar.selectbox
st.sidebar.number_input
St.sidebar.button
'''

import streamlit as st

st.title("Product Management")

with st.sidebar:
    st.header("Add New Product")
    product_name=st.text_input("Product Name")
    
    category = st.selectbox("Category", options=["Electronics", "Home", "Book", "clothing"])
    
    price= st.number_input("Enter the price")
    
    add_button=st.button("Add Product")
    
if add_button:
    if product_name:
        st.success("Product Added Successfully")
        
        st.subheader("Product Details")
        st.write(f"Name:",{product_name})
        st.write(f"Category",{category})
        st.write(f"Price", price)
        
    else:
        st.error("Please enter a product name")
        
