from fastapi import APIRouter
from modules import data_processing
from modules.database import db
from starlette.concurrency import run_in_threadpool
from modules import post_data

router = APIRouter()

@router.post("/waterqualitysub/{table_name}")
async def water_quality_sub(table_name: str, data: dict):
    """
    Subscribe to water quality data updates.

    Args:
        table_name (str): The name of the table to subscribe to.
        data (dict): The data to process.

    Returns:
        dict: The processed data.
    """
    return data_processing.process_water_quality_sub(db, table_name, data)

@router.post("/rawwaterqualitysub/{table_name}")
async def raw_water_quality_sub(table_name: str, data: dict):
    """
    Subscribe to raw water quality data updates.

    Args:
        table_name (str): The name of the table to subscribe to.
        data (dict): The data to process.

    Returns:
        dict: The processed data.
    """
    return data_processing.process_raw_water_quality_sub(db, table_name, data)

@router.post("/waterlevelsub/{table_name}")
async def water_level_sub(table_name: str, data: dict):
    """
    Subscribe to water level data updates.

    Args:
        table_name (str): The name of the table to subscribe to.
        data (dict): The data to process.

    Returns:
        dict: The processed data.
    """
    return data_processing.process_water_level_sub(db, table_name, data)

@router.post("/motorsub/{table_name}")
async def motor_sub(table_name: str, data: dict):
    """
    Subscribe to motor data updates.

    Args:
        table_name (str): The name of the table to subscribe to.
        data (dict): The data to process.

    Returns:
        dict: The processed data.
    """
    return data_processing.process_motor_sub(db, table_name, data)

@router.post("/waterflowsub/{table_name}")
async def water_flow_sub(table_name: str, data: dict):
    """
    Subscribe to water flow data updates.

    Args:
        table_name (str): The name of the table to subscribe to.
        data (dict): The data to process.

    Returns:
        dict: The processed data.
    """
    return data_processing.process_water_flow_sub(db, table_name, data)

@router.post("/actuationsub/{table_name}")
async def node_act_sub(table_name: str, data: dict):
    """
    Subscribe to node actuation data updates.This helps to store the actuations from onem2m to the dataabse.

    Args:
        table_name (str): The name of the table to subscribe to.
        data (dict): The data to process.

    Returns:
        dict: The processed data.
    """
    return data_processing.process_node_act_sub(db, table_name, data)
    
    

@router.post("/actuation/{node_type}/{node_name}/{status}")
async def node_act(node_type: str,node_name: str, status: str):
    """
    Perform node actuation.

    Args:
        node_type (str): The type of the node.
        node_name (str): The name of the node.
        status (str): The status of the actuation.

    Returns:
        dict: The result of the actuation.
    """
    return post_data.post_to_onem2m_act(node_type , node_name, status)

