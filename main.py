from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel
import json
import psycopg2

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define your PostgreSQL connection parameters
DB_NAME = 'zf_digitaltwin'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()

# Define a Pydantic model for the incoming data
class SensorData(BaseModel):
    con: str
    ct: str

@app.post("/incoming-data/{table_name}")
async def incoming_data(table_name: str, data: dict):
    try:
        # Extract data from the received JSON
        cin = data.get('m2m:sgn', {}).get('m2m:nev', {}).get('m2m:rep', {}).get('m2m:cin', {}).get('con', None)
        if cin is None:
            raise HTTPException(status_code=400, detail='Invalid request format. Missing "con" field.')

        # Parse the "con" values
        con_values = json.loads(cin)

        # Check if any value is NaN, and handle it accordingly
        if any(map(lambda x: x != x, con_values)):
            raise HTTPException(status_code=400, detail='Invalid con values. Please check the format.')

        # Extract creation time
        creation_time = data.get('m2m:sgn', {}).get('m2m:nev', {}).get('m2m:rep', {}).get('m2m:cin', {}).get('ct', None)
        if creation_time is None:
            raise HTTPException(status_code=400, detail='Invalid request format. Missing "ct" field.')

        # Format the timestamp
        timestamp = creation_time.replace('T', ' ').replace('Z', '')

        # Build the insert statement dynamically
        insert_statement = f"""
            INSERT INTO {table_name} 
            (creationtime, temperature, voltage, uncompensated_tds, compensated_tds) 
            VALUES (%s, %s, %s, %s, %s)
        """
        
        # Insert data into PostgreSQL database
        cur.execute(
            insert_statement,
            [
                timestamp,
                con_values[0], # temperature
                con_values[1], # voltage
                con_values[2], # uncompensated_tds
                con_values[3]  # compensated_tds
            ]
        )
        conn.commit()

        print('Data inserted successfully into table:', table_name)
        return {'message': 'Data received and inserted successfully.'}
    except Exception as e:
        print('Error inserting data into PostgreSQL:', str(e))
        raise HTTPException(status_code=500, detail='Internal Server Error')
    
# Testing Code  
# @app.post("/incoming-data/{table_name}")
# async def incoming_data(table_name: str, data: dict):
#     try:
#         # Extract data from the received JSON
#         cin = data.get('m2m:sgn', {}).get('m2m:nev', {}).get('m2m:rep', {}).get('m2m:cin', {})
#         print(f'Received data for table {table_name}:', cin)
#         return {'message': 'Data received successfully.'}
#     except Exception as e:
#         print('Error processing data:', str(e))
#         raise HTTPException(status_code=500, detail='Internal Server Error')

    
if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8080)