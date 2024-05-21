import psycopg2
import os
from dotenv import load_dotenv

class Database:
    def __init__(self):
        dotenv_path = os.path.dirname(__file__)
        dotenv_path=os.path.dirname(dotenv_path)
        dotenv_path = os.path.join(dotenv_path, '.env')
        print("ENV PATH: ", dotenv_path)
        load_dotenv(dotenv_path)
        # Define your PostgreSQL connection parameters
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
        print(f"Environment variables loaded successfully:\nDB_NAME={self.DB_NAME}\nDB_USER={self.DB_USER}\nDB_PASSWORD={self.DB_PASSWORD}\nDB_HOST={self.DB_HOST}\nDB_PORT={self.DB_PORT}")
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
        sql_file = os.path.join(os.path.dirname(__file__), '../sql', 'postgres_tables.sql')
        with open(sql_file, 'r') as file:
            sql_statements = file.read()

        # Split SQL statements into individual statements
        statements = sql_statements.split(';')

        # Execute each SQL statement
        try:
            for statement in statements:
                # Remove leading/trailing whitespace and skip empty statements
                statement = statement.strip()
                if statement:
                    # Attempt to execute the SQL statement
                    self.cur.execute(statement)
            self.conn.commit()
        except Exception as e:
            # Handle any exceptions that occur during table creation
            print(f"Error creating tables: {str(e)}")
            self.conn.rollback()

#Creating a DB instance class
db = Database()