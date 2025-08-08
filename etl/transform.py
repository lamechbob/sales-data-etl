
def createDatabasePro(conn):
    """
    Drops and recreates the 'sales' table in the connected PostgreSQL database.
    This ensures a fresh schema on every run.
    """
    cursor = conn.cursor()

    # Drop the table if it already exists
    print('-- Dropping existing sales table if it exists')
    cursor.execute("DROP TABLE IF EXISTS sales;")

    # Create a new table with appropriate columns and types
    print('-- Creating new sales table')
    cursor.execute("""
        CREATE TABLE sales (
            sale_id INTEGER PRIMARY KEY, 
            product TEXT,
            quantity INTEGER, 
            price_per_unit REAL, 
            sale_date TEXT
        );
    """)
    print('-- Sales table created successfully')


def updateTablePro(conn, sales_data_df):
    """
    Inserts rows from the provided DataFrame into the 'sales' table.

    Parameters:
    - conn: An open pg8000 database connection
    - sales_data_df: pandas DataFrame with the sales data
    """
    cursor = conn.cursor()

    print('-- Inserting records into sales table')

    # Iterate through each row in the DataFrame and insert into the table
    for index, row in sales_data_df.iterrows():
        cursor.execute("""
            INSERT INTO sales (sale_id, product, quantity, price_per_unit, sale_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            row['sale_id'],
            row['product'],
            row['quantity'],
            row['price_per_unit'],
            row['sale_date']
        ))

        # Optional: Print confirmation for each row (can be commented out in production)
        print(
            f"Inserted: {row['sale_id']} | {row['product']} | {row['quantity']} | {row['price_per_unit']} | {row['sale_date']}")

    print('-- All records inserted successfully')
