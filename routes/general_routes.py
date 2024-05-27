from fastapi import APIRouter
from modules import data_processing
from modules.database import db
from starlette.concurrency import run_in_threadpool
from modules import post_data


router = APIRouter()

@router.post("/calibdata")
async def node_act_sub(data: dict):
    """
    Process calibration data.This is used in the form which is deployed to collect the data from the nodes manually.

    Args:
        data (dict): The calibration data to process.

    Returns:
        dict: The processed data.
    """
    result = await run_in_threadpool(data_processing.process_calibdata,db, data)
    return result

@router.get("/get_value")
async def get_value(table_name: str):
    """
    Get real-time data.

    Args:
        table_name (str): The name of the table to fetch data from.

    Returns:
        dict: The fetched data.
    """
    result = await run_in_threadpool(data_processing.get_real_time_data, db, table_name)
    return result

