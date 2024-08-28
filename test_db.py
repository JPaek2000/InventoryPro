from flask import Flask, request, jsonify, render_template
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database connection parameters from environment variables
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

# Function to connect to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(**db_params)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# Retrieves all products from the database and returns them as JSON.
@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products;')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)

# Inserts a new product into the database based on the request data.
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data['name']
    quantity = data['quantity']
    price = data['price']

    conn = get_db_connection()
    cursor = conn.cursor()
    # Insert data into the table
    cursor.execute(
        'INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s);',
        (name, quantity, price)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
