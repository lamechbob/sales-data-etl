import sqlite3
import pandas as pd

from etl import transform as trans

database_name = 'sales.db'

# ------------------------
# 1. READ SALES DATA
# ------------------------

# Load sales data from CSV into a Pandas DataFrame
sales_data_df = pd.read_csv('data/sales_data.csv')

# Preview the first few rows of data
print('-- Example Sales Data')
print(sales_data_df.head())

# ------------------------
# 2. CREATE DATABASE + TABLE
# ------------------------

trans.createDatabase(database_name)

# ------------------------
# 3. LOAD DATA INTO TABLE
# ------------------------

trans.updateTable(database_name,sales_data_df)

# ------------------------
# 4. RUN SQL QUERIES
# ------------------------

trans.runCalculations(database_name)