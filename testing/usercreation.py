import psycopg2
from passlib.context import CryptContext

# Database connection details

DATABASE_USER = input("Enter Database Username: ")
DATABASE_PASSWORD = input("Enter Database Password: ")
DATABASE_NAME = input("Enter Database Name: ")

# Create a connection to the database
conn = psycopg2.connect(
    dbname=DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host="localhost"
)

# Create a cursor object
cursor = conn.cursor()

# Password context for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User details
username = input("Enter Username: ")
password = input("Enter Password: ")
hashed_password = pwd_context.hash(password)

# Insert query
insert_query = """
INSERT INTO users (username, hashed_password)
VALUES (%s, %s)
"""
cursor.execute(insert_query, (username, hashed_password))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
