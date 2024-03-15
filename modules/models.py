from pydantic import BaseModel

# Define Pydantic models for your application

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
    applied_pressure: float = 300000
    hydraulic_pressure_drop: float = 50000
    dynamic_viscosity: float = 0.0009
    membrane_permeability: float = 5e-9
    effective_membrane_area: float = 1
    molar_concentration: float = 0.01
    voltage: float = 10.0
    temperature: float = 30.0
