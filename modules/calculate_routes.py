from fastapi import APIRouter
from modules import calculation

router = APIRouter()

@router.post("/calculate")
async def calculate_simulation(input_data: calculation.SimulationInput):
    return calculation.calculate_simulation(input_data)

@router.post("/calculate_ro_filtration")
def calculate_ro_filtration(params: calculation.ROFiltrationRequest):
    return calculation.calculate_ro_filtration(params)
