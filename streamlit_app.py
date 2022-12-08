# Import necessary libraries
import streamlit as st

# Prompt user for input
st.title("Bill of Materials Generator")

# Create a dropdown menu for the country
countries = ["USA", "Canada", "Mexico"]
country = st.selectbox("Select country:", countries)

# Create a dropdown menu for the merchant
merchants = ["Amazon", "Walmart", "Target"]
merchant = st.selectbox("Select merchant:", merchants)

# Create an input field for the store name
store_name = st.text_input("Enter store name:")

# Create an input field for the operational hours
operational_hours = st.text_input("How many hours is Prime Now Operating per day:")

# Create an input field for the staging area
staging_area = st.text_input("Staging area (in SQM):")

# Create an input field for the non-inventory area
non_inventory = st.text_input("Non-inventory (in SQM):")

# Create an input field for the chill chain area
chill_chain = st.text_input("Chill chain (in SQM):")

# Display the input fields
st.write("Country:", country)
st.write("Merchant:", merchant)
st.write("Store Name:", store_name)
st.write("Operational Hours:", operational_hours)
st.write("Staging Area:", staging_area)
st.write("Non-Inventory Area:", non_inventory)
st.write("Chill Chain Area:", chill_chain)
