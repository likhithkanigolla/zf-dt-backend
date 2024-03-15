from fastapi import APIRouter
from .models import SimulationInput, ROFiltrationRequest

router = APIRouter()

@router.post("/calculate")
async def calculate_simulation(input_data: SimulationInput):
    return calculate_simulation(input_data)

@router.post("/calculate_ro_filtration")
def calculate_ro_filtration(params: ROFiltrationRequest):
    return calculate_ro_filtration(params)
