import sqlite3
import pandas as pd
def createDatabase(database_name):

    # Create a SQLite database connection (will create 'sales.db' if it doesn't exist)
    conn = sqlite3.connect(database_name)

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

def updateTable(database_name,sales_data_df):

    # Create a SQLite database connection (will create 'sales.db' if it doesn't exist)
    conn = sqlite3.connect(database_name)

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

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

    conn.commit()
    conn.close()

def runCalculations(database_name):

    # Create a SQLite database connection (will create 'sales.db' if it doesn't exist)
    conn = sqlite3.connect(database_name)

    # Create a cursor object to execute SQL commands
    c = conn.cursor()

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
    # DISPLAY RESULTS
    # ------------------------

    print('\n-- Total Sales Per Transaction')
    print(total_sales_per_transaction)

    # Pull the first result as the "highest single sale" (most revenue in one transaction)
    print('\n-- Highest Single Sale')
    highest_single_sale = total_sales_per_transaction[0]
    print(highest_single_sale)

    print('\n-- Top 3 Transactions By Volume')
    print(top_3_by_quantity)

    conn.close()

def codeChallengeWeek3(dirty_sales_file_path):

    '''
    Write a function that:

    - Accepts a file path and returns a cleaned DataFrame:
        - Drops null values
        - Lowercases column names
    - Saves the result to: `outputs/cleaned_sales.csv`
    '''

    # Get Data
    dirty_sales_df = pd.read_csv(dirty_sales_file_path)

    # Drop rows with Null values
    dirty_sales_df = dirty_sales_df.dropna()

    print('\nClean Dirty Sales Data')
    print(dirty_sales_df)

    # Convert all column names to lowercase
    dirty_sales_df.columns = dirty_sales_df.columns.str.lower()

    print('\nLower Case Column Names')
    print(dirty_sales_df)

    # Export Data to File
    dirty_sales_df.to_csv('outputs/cleaned_sales.csv',index=False)