from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from pydantic import BaseModel
import json
import psycopg2
import math

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
DB_USER = 'likhith'
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
    
class SimulationInput(BaseModel):
    number1: float
    number2: float
    number3: float
    number4: float
    
class ROFiltrationRequest(BaseModel):
    initial_tds: float = 800
    desired_tds: float = 50
    applied_pressure: float = 101325
    hydraulic_pressure_drop: float = 10000
    dynamic_viscosity: float = 0.001
    membrane_permeability: float = 1e-9
    effective_membrane_area: float = 1
    molar_concentration: float = 0.01
    voltage: float = 10.0
    temperature: float = 30.0

# Constants
R = 8.314  # Ideal gas constant (J/(mol·K))
T = 298.15  # Temperature (25°C in Kelvin)
i = 1  # van't Hoff factor (assumed for simplicity)

# Function to calculate osmotic pressure
def calculate_osmotic_pressure(C):
    return i * C * R * T

# Function to calculate water flux
def calculate_water_flux(P, delta_P, mu, L):
    return L * (P - delta_P) / mu

# Function to calculate permeate flow rate
def calculate_permeate_flow_rate(A, water_flux):
    return A * water_flux

# Function to calculate TDS reduction
def calculate_tds_reduction(initial_tds, permeate_flow_rate, tds_reduction_rate):
    return initial_tds - tds_reduction_rate * permeate_flow_rate

# Function to calculate TDS value based on voltage and temperature
def calculate_tds(voltage, temperature):
    CV = voltage / (1.0 + 0.02 * (temperature - 25))
    return 133.42 * (CV ** 3) - 255.86 * (CV ** 2) + 857.39 * CV * 0.5


def process_data(table_name: str, data: dict, column_order: list):
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
            (creationtime, {', '.join(column_order)}) 
            VALUES (%s, {', '.join(['%s' for _ in range(len(column_order))])})
        """
        
        # Insert data into PostgreSQL database
        cur.execute(
            insert_statement,
            [timestamp] + [con_values[i] for i in range(len(column_order))]
        )
        conn.commit()

        print('Data inserted successfully into table:', table_name)
        return {'message': 'Data received and inserted successfully.'}
    except Exception as e:
        print('Error inserting data into PostgreSQL:', str(e))
        raise HTTPException(status_code=500, detail='Internal Server Error')

@app.post("/waterqualitysub/{table_name}")
async def water_quality_sub(table_name: str, data: dict):
    return process_data(table_name, data, ['temperature', 'voltage', 'uncompensated_tds', 'compensated_tds'])

@app.post("/waterlevelsub/{table_name}")
async def water_level_sub(table_name: str, data: dict):
    return process_data(table_name, data, ['waterlevel', 'temperature'])

@app.post("/motorsub/{table_name}")
async def water_level_sub(table_name: str, data: dict):
    return process_data(table_name, data, ['status', 'current'])

@app.post("/roplantsub/{table_name}")
async def water_level_sub(table_name: str, data: dict):
    return process_data(table_name, data, ['tds'])

@app.post("/calculate")
async def calculate_simulation(input_data: SimulationInput):
    try:
        # Perform calculation (example: sum of numbers)
        result = input_data.number1 + input_data.number2 + input_data.number3 + input_data.number4
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@app.post("/calculate_ro_filtration")
def calculate_ro_filtration(params: ROFiltrationRequest):
    # Get parameters from request
    initial_tds = params.initial_tds
    desired_tds = params.desired_tds
    P = params.applied_pressure
    delta_P = params.hydraulic_pressure_drop
    mu = params.dynamic_viscosity
    L = params.membrane_permeability
    A = params.effective_membrane_area
    C = params.molar_concentration
    voltage = params.voltage
    temperature = params.temperature
    
    # Calculate osmotic pressure
    osmotic_pressure = calculate_osmotic_pressure(C)

    # Calculate water flux
    water_flux = calculate_water_flux(P, delta_P, mu, L)

    # Calculate permeate flow rate
    permeate_flow_rate = calculate_permeate_flow_rate(A, water_flux)

    # Calculate TDS reduction
    tds_reduction_rate = 0.05  # Example TDS reduction rate (ppm/s·m²)
    tds_final = calculate_tds_reduction(initial_tds, permeate_flow_rate, tds_reduction_rate)

    # Calculate TDS value based on voltage and temperature
    tds_calculated = calculate_tds(voltage, temperature)

    return {
        "osmotic_pressure": osmotic_pressure,
        "water_flux": water_flux,
        "permeate_flow_rate": permeate_flow_rate,
        "final_tds_concentration_after_ro_tank": tds_final,
        "calculated_tds_value": tds_calculated
    }  

    
if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=1629)