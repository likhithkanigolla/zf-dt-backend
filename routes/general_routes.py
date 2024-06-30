from fastapi import APIRouter, HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
from modules import data_processing,alarms,notifications
from modules.database import db
from modules.models import LogData
from starlette.concurrency import run_in_threadpool
from modules import post_data, telegram
import asyncio,os
from datetime import datetime



router = APIRouter()


# Predefined node IDs
water_quality_nodes = ["WM-WD-KH98-00","WM-WD-KH96-00","WM-WD-KH96-01", "WM-WD-KH96-02", "WM-WD-KH95-00", "WM-WD-KH03-00"]
other_nodes = [
    "WM-WF-KH95-40", "WM-WL-KH98-00", "DM-KH98-60", "WM-WF-KH98-40", 
    "WM-WL-KH00-00", "WM-WF-KB04-70", "WM-WF-KB04-73", "WM-WF-KB04-71", "WM-WF-KB04-72",
]


# water_quality_nodes = [
#     "WM-WD-KH96-00",
# ]
# other_nodes = ["WM-WL-KH98-00"]

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

# @router.post("/telegram")
# async def send_telegram(node_name:str, time:str):
#     return telegram.check_node_status(node_name,time, db)


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


@router.get("/notifications")
# Get all notifications from the database
async def read_notifications():
    return await run_in_threadpool(notifications.read_notifications, db)

@router.post("/create/notification")
# Insert a notification into the database
async def insert_notification(data: dict):
    return await run_in_threadpool(notifications.insert_notification, db, data)


@router.put("/{id}/notification/read")
# Update the notification as read in the database
async def read_notification(id: str):
    return await run_in_threadpool(notifications.update_notification, db, id)


@router.get("/alarms")
# Get all alarms from the database
async def read_alarms():
    return await run_in_threadpool(alarms.read_alarms, db)

@router.post("/create/alarm")
# Insert an alarm into the database
async def insert_alarm(data: dict):
    return await run_in_threadpool(alarms.insert_alarm, db, data)

@router.put("/{id}/alarm/resolve")
# Update the alarm as read in the database
async def read_alarm(id: str, remarks: dict):
    return await run_in_threadpool(alarms.update_alarm, db, id, remarks)

@router.post("/save_log")
async def save_log(request: Request):
    return await data_processing.save_log_to_file(request)


