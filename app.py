import sqlite3
import pandas as pd

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

# Create a SQLite database connection (will create 'sales.db' if it doesn't exist)
conn = sqlite3.connect('sales.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Drop the sales table if it already exists (ensures a fresh load each time)
with conn:
    c.execute("DROP TABLE IF EXISTS sales;")
    print('-- Drop Sales Table')

# Create a new sales table with appropriate columns and data types
with conn:
    c.execute("""
        CREATE TABLE sales (
            sale_id INTEGER PRIMARY KEY, 
            product TEXT,
            quantity INTEGER, 
            price_per_unit REAL, 
            sale_date TEXT
        );
    """)
    print('-- Create Sales Table')

# ------------------------
# 3. LOAD DATA INTO TABLE
# ------------------------

print('-- Update Sales Table')

# Insert each row from the DataFrame into the SQLite table
for index, row in sales_data_df.iterrows():
    c.execute("""
        INSERT INTO sales VALUES (:sale_id, :product, :quantity, :price_per_unit, :sale_date)
    """, {
        'sale_id': row['sale_id'],
        'product': row['product'],
        'quantity': row['quantity'],
        'price_per_unit': row['price_per_unit'],
        'sale_date': row['sale_date']
    })

    # Print confirmation of the inserted row
    print(f"{row['sale_id']} {row['product']} {row['quantity']} {row['price_per_unit']} {row['sale_date']}")

# ------------------------
# 4. RUN SQL QUERIES
# ------------------------

print('-- Executing Calculations')

# Query: Total sales per transaction (can be adjusted to total per product if needed)
total_sales_per_transaction = c.execute("""
    SELECT sale_id, product, (quantity * price_per_unit) AS total_sales
    FROM sales
    ORDER BY total_sales DESC;
""").fetchall()

# Query: Top 3 transactions with the highest quantity sold
top_3_by_quantity = c.execute("""
    SELECT sale_id, product, quantity
    FROM sales
    ORDER BY quantity DESC
    LIMIT 3;
""").fetchall()

# ------------------------
# 5. DISPLAY RESULTS
# ------------------------

print('-- Total Sales Per Transaction')
print(total_sales_per_transaction)

# Pull the first result as the "highest single sale" (most revenue in one transaction)
print('-- Highest Single Sale')
highest_single_sale = total_sales_per_transaction[0]
print(highest_single_sale)

print('-- Top 3 Transactions By Volume')
print(top_3_by_quantity)
