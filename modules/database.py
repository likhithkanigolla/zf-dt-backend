import psycopg2

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
