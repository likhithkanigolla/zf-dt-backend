from .models import SensorData
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
            INSERT INTO {table_name} 
            (creationtime, {', '.join(column_order)}) 
            VALUES (%s, {', '.join(['%s' for _ in range(len(column_order))])})
        """

        db.cur.execute(
            insert_statement,
            [timestamp] + [con_values[i] for i in range(len(column_order))]
        )
        db.conn.commit()

        print('Data inserted successfully into table:', table_name)
        return {'message': 'Data received and inserted successfully.'}
    except Exception as e:
        print('Error inserting data into PostgreSQL:', str(e))
        raise ValueError('Internal Server Error')

def process_water_quality_sub(db, table_name, data):
    return process_data(db, table_name, data, ['temperature', 'voltage', 'uncompensated_tds', 'compensated_tds'])

def process_water_level_sub(db, table_name, data):
    return process_data(db, table_name, data, ['waterlevel', 'temperature'])

def process_motor_sub(db, table_name, data):
    return process_data(db, table_name, data, ['status', 'current'])

def process_ro_plant_sub(db, table_name, data):
    return process_data(db, table_name, data, ['tds'])
