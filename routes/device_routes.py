from fastapi import APIRouter
from modules import data_processing
from modules.database import db
from starlette.concurrency import run_in_threadpool

router = APIRouter()

@router.post("/waterqualitysub/{table_name}")
async def water_quality_sub(table_name: str, data: dict):
    return data_processing.process_water_quality_sub(db, table_name, data)

@router.post("/rawwaterqualitysub/{table_name}")
async def raw_water_quality_sub(table_name: str, data: dict):
    return data_processing.process_raw_water_quality_sub(db, table_name, data)

@router.post("/waterlevelsub/{table_name}")
async def water_level_sub(table_name: str, data: dict):
    return data_processing.process_water_level_sub(db, table_name, data)

@router.post("/motorsub/{table_name}")
async def motor_sub(table_name: str, data: dict):
    return data_processing.process_motor_sub(db, table_name, data)

@router.post("/waterflowsub/{table_name}")
async def motor_sub(table_name: str, data: dict):
    return data_processing.process_water_flow_sub(db, table_name, data)

@router.get("/get_value")
async def get_value(table_name: str):
    # Execute the synchronous DB operation in a thread pool
    result = await run_in_threadpool(data_processing.get_real_time_data, db, table_name)
    return result

