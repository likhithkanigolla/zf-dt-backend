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
    sump_capacity: float=100
    timeMultiplier: int = 1

class SoilContaminationRequest(BaseModel):
    temperature: float = 27.125
    sumpCapacity: float = 60000
    SoilQuantiy: float = 200
    
class SandContaminationRequest(BaseModel):
    temperature: float = 27.125
    sumpCapacity: float = 60000
    SandQuantiy: float = 200
    
class MotorFlowRateRequest(BaseModel):
    voltage: float = 220
    current: float = 10.11
    power_factor: float = 0.11
    motor_efficiency: float = 0.85
    depth: float = 3
    timeMultiplier: int = 1