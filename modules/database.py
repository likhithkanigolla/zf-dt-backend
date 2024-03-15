import psycopg2
import os

class Database:
    def __init__(self):
        # Define your PostgreSQL connection parameters
        self.DB_NAME = 'zf_digitaltwin'
        self.DB_USER = 'likhith'
        self.DB_PASSWORD = 'postgres'
        self.DB_HOST = 'localhost'
        self.DB_PORT = '5432'

        # Connect to PostgreSQL
        self.conn = psycopg2.connect(
            dbname=self.DB_NAME,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=self.DB_PORT
        )
        self.cur = self.conn.cursor()

        # Check and create tables from SQL file
        self.create_tables()

    def create_tables(self):
        # Read SQL file
        sql_file = os.path.join(os.path.dirname(__file__), 'sql', 'postgres_tables.sql')
        with open(sql_file, 'r') as file:
            sql_statements = file.read()

        # Execute SQL statements
        self.cur.execute(sql_statements)
        self.conn.commit()
