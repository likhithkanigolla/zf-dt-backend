from fastapi import APIRouter
from modules import data_processing
from modules.database import db
from starlette.concurrency import run_in_threadpool
from modules import post_data, telegram
import asyncio


router = APIRouter()

# Predefined node IDs
water_quality_nodes = ["WM-WD-KH98-00","WM-WD-KH96-00","WM-WD-KH96-01", "WM-WD-KH04-00", "WM-WD-KH95-00", "WM-WD-KH03-00"]
other_nodes = [
    "WM-WF-KH95-40", "WM-WD-KH98-00", "WM-WL-KH98-00", "DM-KH98-60", 
    "WM-WF-KH98-40", "WM-WD-KH96-00", "WM-WL-KH00-00", "WM-WF-KB04-70", 
    "WM-WF-KB04-73", "WM-WD-KH96-01", "WM-WD-KH04-00", "WM-WF-KB04-71", 
    "WM-WF-KB04-72", "WM-WD-KH95-00", "WM-WD-KH03-00"
]


# water_quality_nodes = [
#     "WM-WD-KH96-00","WM-WL-KH98-00"
# ]

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

@router.post("/telegram")
async def send_telegram(node_name:str, time:str):
    return telegram.check_node_status(node_name,time, db)


async def check_waterquality_node_status_periodically():
    while True:
        for node_id in water_quality_nodes:
            await telegram.check_node_status(node_id, "3h", db)
        await asyncio.sleep(1800)  # Wait for 30 minutes
        
async def check_node_status_periodically():
    while True:
        for node_id in other_nodes:
            await telegram.check_node_status(node_id, "10m", db)
        await asyncio.sleep(600)  # Wait for 10 minutes

# Start the periodic task
asyncio.create_task(check_node_status_periodically())
asyncio.create_task(check_waterquality_node_status_periodically())
