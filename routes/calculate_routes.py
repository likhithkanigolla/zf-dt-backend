from fastapi import APIRouter
from modules.models import SimulationInput, ROFiltrationRequest 
from modules.calculation import calculate_ro_filtration

router = APIRouter()

@router.post("/calculate")
async def calculate_simulation(input_data: SimulationInput):
    return calculate_simulation(input_data)

@router.post("/calculate_ro_filtration")
def calculate_ro_filtration_pass(params: ROFiltrationRequest):
    return calculate_ro_filtration(params)
