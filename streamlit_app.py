# Import necessary libraries
from sqlalchemy import create_engine
import pandas as pd
from fpdf import FPDF
import streamlit as st

# Set database connection strings and table names
db1_conn_str = "[database_connection_string_1]"
db1_table = "[table_name_1]"
db2_conn_str = "[database_connection_string_2]"
db2_table = "[table_name_2]"
db3_conn_str = "[database_connection_string_3]"
db3_table = "[table_name_3]"

# Create a function to generate the bill of materials
def generate_bill_of_materials(country, merchant, operational_hours, staging_area, chill_chain_area):
    # Connect to database 1 and query it for data
    engine = create_engine(db1_conn_str)
    df1 = pd.read_sql_query("SELECT * FROM %s WHERE country = '%s' AND merchant = '%s'" % (db1_table, country, merchant), engine)

    # Connect to database 2 and query it for data
    engine = create_engine(db2_conn_str)
    df2 = pd.read_sql_query("SELECT * FROM %s WHERE operational_hours = '%s'" % (db2_table, operational_hours), engine)

    # Connect to database 3 and query it for data
    engine = create_engine(db3_conn_str)
    df3 = pd.read_sql_query("SELECT * FROM %s WHERE staging_area = '%s' AND chill_chain_area = '%s'" % (db3_table, staging_area, chill_chain_area), engine)

    # Generate bill of materials based on input
    bill_of_materials = []
    if df1.empty:
        bill_of_materials = [
            {"name": "shelving units", "quantity": 10},
            {"name": "checkout counters", "quantity": 5},
            {"name": "refrigerators", "quantity": 2},
            {"name": "freezers", "quantity": 1},
            {"name": "shopping carts", "quantity": 15},
        ]
    else:
        bill_of_materials = [
            {"name": "shelving units", "quantity": df1["shelving_units"]},
            {"name": "checkout counters", "quantity": df1["checkout_counters"]},
            {"name": "refrigerators", "quantity": df1["refrigerators"]},
            {"name": "freezers", "quantity": df1["freezers"]},
            {"name": "shopping carts", "quantity": df1["shopping_carts"]},
        ]

    # Adjust quantities based on input
    if df2.empty:
        for item in bill_of_materials:
            if item["name"] == "checkout counters
