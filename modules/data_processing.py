from fastapi import HTTPException
from .models import SensorData
from sklearn.linear_model import LinearRegression
import numpy as np
import json

def process_data(db, table_name, data, column_order):
    try:
        # Extract data from the received JSON
        cin = data.get('m2m:sgn', {}).get('m2m:nev', {}).get('m2m:rep', {}).get('m2m:cin', {}).get('con', None)
        if cin is None:
            raise ValueError('Invalid request format. Missing "con" field.')

        con_values = json.loads(cin)
        

        if any(map(lambda x: x != x, con_values)):
            raise ValueError('Invalid con values. Please check the format.')

        creation_time = data.get('m2m:sgn', {}).get('m2m:nev', {}).get('m2m:rep', {}).get('m2m:cin', {}).get('ct', None)
        if creation_time is None:
            raise ValueError('Invalid request format. Missing "ct" field.')

        timestamp = creation_time.replace('T', ' ').replace('Z', '')

        insert_statement = f"""
            INSERT INTO "{table_name}" 
            (creationtime, {', '.join(column_order)}) 
            VALUES (%s, {', '.join(['%s' for _ in range(len(column_order))])})
        """

        db.cur.execute(
            insert_statement,
            [timestamp] + [con_values[i+1] for i in range(len(column_order))]
        )
        db.conn.commit()

        print('Data inserted successfully into table:', table_name)
        return {'message': 'Data received and inserted successfully.'}
    
    except Exception as e:
        print('Error inserting data into PostgreSQL:', str(e))
        raise ValueError('Internal Server Error')

def process_water_quality_sub(db, table_name, data):
    return process_data(db, table_name, data, ['temperature', 'voltage', 'uncompensated_tds', 'compensated_tds'])

def process_raw_water_quality_sub(db, table_name, data):
    return process_data(db, table_name, data, ['temperature', 'voltage', 'uncompensated_tds', 'compensated_tds', 'turbudity', 'ph'])


def process_water_level_sub(db, table_name, data):
    return process_data(db, table_name, data, ['waterlevel', 'temperature'])

def process_motor_sub(db, table_name, data):
    return process_data(db, table_name, data, ['status', 'voltage','current','power','energy','frequency','power_factor'])

def process_ro_plant_sub(db, table_name, data):
    return process_data(db, table_name, data, ['tds'])

def process_water_flow_sub(db, table_name, data):
    return process_data(db, table_name, data, ['flowrate', 'totalflow'])

# Assuming this function is in a module named data_processing.py
def get_real_time_data(db, table_name):
    try:
        # SQL injection risk mitigation - Ensure table_name is validated or sanitized
        # if table_name not in ['allowed_table_1', 'allowed_table_2']:
        #     raise HTTPException(status_code=400, detail="Invalid table name")

        query = f'SELECT * FROM "{table_name}" ORDER BY timestamp DESC LIMIT 1;'
        db.cur.execute(query)
        result = db.cur.fetchone()

        if result:
            # Fetching column names from cursor.description
            columns = [col[0] for col in db.cur.description]
            # Creating a dictionary {column_name: value}
            data = dict(zip(columns, result))
            return data
        else:
            raise HTTPException(status_code=404, detail="Value not found")
    except Exception as e:
        # In a real application, consider more specific exception handling and logging
        print(e)
        raise HTTPException(status_code=500, detail="Database operation failed")

def voltage_calculation(soil_quantity):
    # Define the voltage data
    voltage_data = {
        0: 1.2,
        100: 2.3,
        200: 3.4,
        300: 4.5,
        400: 5.6,
        500: 6.7,
    }

    # Prepare the data for training
    X = np.array(list(voltage_data.keys())).reshape(-1, 1)
    y = np.array(list(voltage_data.values()))

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    if 1 <= soil_quantity <= 500:
        # Predict the voltage for the given soil quantity
        predicted_voltage = model.predict([[soil_quantity]])
        return {"predicted_voltage": predicted_voltage[0]}
    else:
        return {"error": "Soil quantity must be between 1 and 500 grams."}

