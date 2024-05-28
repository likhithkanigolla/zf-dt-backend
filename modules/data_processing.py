from fastapi import HTTPException
from .models import SensorData
from sklearn.linear_model import LinearRegression
import numpy as np
import json
from fastapi import HTTPException
from .models import SensorData
from sklearn.linear_model import LinearRegression
import numpy as np
import json
import psycopg2
from psycopg2 import Error

def process_data(db, table_name, data, column_order):
    """
    Process and insert data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.

        data (dict): The data to be processed and inserted.
        column_order (list): The order of columns in the table.

    Returns:
        dict: A dictionary with a success message.


    Raises:
        ValueError: If there is an error in the request format or con values.
    """

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
        try:
            db.cur.execute(
            insert_statement,
            [timestamp] + [con_values[i+1] for i in range(len(column_order))]
            )
            db.conn.commit()
            print('Data inserted successfully into table:', table_name)
            return {'message': 'Data received and inserted successfully.'}
        except psycopg2.errors.InFailedSqlTransaction as e:
            print('Error inserting data into PostgreSQL:', str(e))
            db.conn.rollback()
            db.reset_connection()  # Reset the database connection
            return {'message': 'DB Connection Reset successfully.'}
    except Exception as e:
        print('Error inserting data into PostgreSQL:', str(e))
        raise ValueError('Internal Server Error')
    
def process_str_data(db, table_name, data, column_order):
    """
    Process and insert string data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.
        data (dict): The data to be processed and inserted.
        column_order (list): The order of columns in the table.

    Returns:
        dict: A dictionary with a success message.

    Raises:

        ValueError: If there is an error in the request format or con values.
    """
    try:
        # Extract data from the received JSON
        cin = data.get('m2m:sgn', {}).get('m2m:nev', {}).get('m2m:rep', {}).get('m2m:cin', {}).get('con', None)
        if cin is None:
            raise ValueError('Invalid request format. Missing "con" field.')
        print("Received con:", type(cin), cin.replace("'",""))
        # con_values = json.loads(cin.replace("'",""))
        con_values = cin.strip('[]').split(',')
        con_values = [val.strip() if val.strip().isdigit() else f'"{val.strip()}"' for val in con_values]
        json_data = json.loads('[' + ', '.join(con_values) + ']')

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

        try:
            db.cur.execute(
            insert_statement,
            [timestamp] + [con_values[i+1].replace("'", "").replace('"', '') for i in range(len(column_order))]
            )
            db.conn.commit()
            print('Data inserted successfully into table:', table_name)
            return {'message': 'Data received and inserted successfully.'}
        except psycopg2.errors.InFailedSqlTransaction as e:
            print('Error inserting data into PostgreSQL:', str(e))
            db.conn.rollback()
            db.reset_connection()  # Reset the database connection
            return {'message': 'DB Connection Reset successfully.'}
    except Exception as e:
        print('Error inserting data into PostgreSQL:', str(e))
        raise ValueError('Internal Server Error')


def process_calibdata(db, data):
    """
    Process and insert calibration data into the "calibdata" table in the database.

    Args:
        db (Database): The database connection object.
        data (dict): The calibration data to be inserted.

    Returns:

        dict: A dictionary with a success message or an error message.

    Raises:
        Exception: If there is an error in the database operation.
    """
    node = data.get('node')
    temperature = data.get('temperature')
    tds = data.get('tds')
    ph = data.get('ph')
    try:
        # Execute the SQL query to insert data into the table
        db.cur.execute(
            "INSERT INTO calibdata (node, temperature, tds, ph) VALUES (%s, %s, %s, %s)",
            (node, temperature, tds, ph)
        )
        # Commit the transaction
        db.conn.commit()
        return {"message": "Data inserted successfully"}
    except psycopg2.errors.InFailedSqlTransaction as e:
        print('Error inserting data into PostgreSQL:', str(e))
        db.conn.rollback()
        db.reset_connection()  # Reset the database connection
        return {'message': 'DB Connection Reset successfully.'}
    except Exception as e:
        # Rollback the transaction if an error occurs
        db.conn.rollback()
        return {"error": str(e)}




def process_water_quality_sub(db, table_name, data):
    """

    Process and insert water quality data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.
        data (dict): The water quality data to be processed and inserted.

    Returns:
        dict: A dictionary with a success message.

    Raises:
        ValueError: If there is an error in the request format or con values.
    """
    return process_data(db, table_name, data, ['temperature', 'voltage', 'uncompensated_tds', 'compensated_tds'])

def process_raw_water_quality_sub(db, table_name, data):
    """


    Process and insert raw water quality data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.
        data (dict): The raw water quality data to be processed and inserted.

    Returns:
        dict: A dictionary with a success message.

    Raises:
        ValueError: If there is an error in the request format or con values.
    """
    return process_data(db, table_name, data, ['temperature', 'voltage', 'uncompensated_tds', 'compensated_tds', 'turbudity', 'ph'])

def process_water_level_sub(db, table_name, data):
    """

    Process and insert water level data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.
        data (dict): The water level data to be processed and inserted.

    Returns:
        dict: A dictionary with a success message.

    Raises:
        ValueError: If there is an error in the request format or con values.
    """
    return process_data(db, table_name, data, ['waterlevel', 'temperature'])

def process_motor_sub(db, table_name, data):
    """

    Process and insert motor data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.
        data (dict): The motor data to be processed and inserted.

    Returns:
        dict: A dictionary with a success message.

    Raises:
        ValueError: If there is an error in the request format or con values.
    """
    return process_data(db, table_name, data, ['status', 'voltage','current','power','energy','frequency','power_factor'])

def process_ro_plant_sub(db, table_name, data):
    """

    Process and insert RO plant data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.
        data (dict): The RO plant data to be processed and inserted.

    Returns:
        dict: A dictionary with a success message.

    Raises:
        ValueError: If there is an error in the request format or con values.
    """
    return process_data(db, table_name, data, ['tds'])

def process_water_flow_sub(db, table_name, data):
    """

    Process and insert water flow data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.
        data (dict): The water flow data to be processed and inserted.

    Returns:
        dict: A dictionary with a success message.

    Raises:
        ValueError: If there is an error in the request format or con values.
    """
    return process_data(db, table_name, data, ['flowrate', 'totalflow'])

def process_node_act_sub(db, table_name, data):
    """

    Process and insert node activity data into the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to insert the data into.
        data (dict): The node activity data to be processed and inserted.

    Returns:
        dict: A dictionary with a success message.

    Raises:
        ValueError: If there is an error in the request format or con values.
    """
    return process_str_data(db, table_name, data, ['node_type', 'status'])

def get_real_time_data(db, table_name):
    """
    Get the latest data from the specified table in the database.

    Args:
        db (Database): The database connection object.
        table_name (str): The name of the table to retrieve data from.

    Returns:
        dict: A dictionary with the latest data.

    Raises:
        HTTPException: If the table name is invalid or the database operation fails.

    """
    try:
        #SQL injection risk mitigation - Ensure table_name is validated or sanitized
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
    except psycopg2.errors.InFailedSqlTransaction as e:
        print('Error inserting data into PostgreSQL:', str(e))
        db.conn.rollback()
        db.reset_connection()  # Reset the database connection
        return {'message': 'DB Connection Reset successfully.'}
    except Exception as e:
        # In a real application, consider more specific exception handling and logging
        print(e)
        raise HTTPException(status_code=500, detail="Database operation failed")


def voltage_calculation(soil_quantity):
    """
    Calculate the predicted voltage based on the given soil quantity.

    Args:
        soil_quantity (int): The quantity of soil in grams.

    Returns:
        dict: A dictionary with the predicted voltage or an error message.

    """
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

