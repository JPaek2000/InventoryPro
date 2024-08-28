import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters from environment variables
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    print("Database connection successful.")
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        quantity INTEGER,
        price DECIMAL(10, 2)
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created successfully or already exists.")
    
    # Insert data into the table
    insert_query = '''
    INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s);
    '''
    cursor.execute(insert_query, ('Widget', 10, 19.99))
    cursor.execute(insert_query, ('Gadget', 5, 29.99))
    cursor.execute(insert_query, ('Thingamajig', 7, 9.99))
    conn.commit()
    print("Data inserted successfully.")
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

except Exception as e:
    print("Error:", e)
