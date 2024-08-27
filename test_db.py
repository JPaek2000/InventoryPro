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

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    print("Database connection successful.")
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Execute a simple SQL query
    cursor.execute("SELECT version();")
    
    # Fetch and print the version
    db_version = cursor.fetchone()
    print("PostgreSQL version:", db_version)
    
    # Close the cursor and connection
    cursor.close()
    conn.close()

except Exception as e:
    print("Error connecting to the database:", e)
