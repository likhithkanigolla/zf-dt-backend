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
    Subscribe to node actuation data updates.

    Args:
        table_name (str): The name of the table to subscribe to.
        data (dict): The data to process.

    Returns:
        dict: The processed data.
    """
    return data_processing.process_node_act_sub(db, table_name, data)
    
@router.post("/calibdata/")
async def node_act_sub(data: dict):
    """
    Process calibration data.

    Args:
        data (dict): The calibration data to process.

    Returns:
        dict: The processed data.
    """
    return data_processing.process_calibdata(db, data)
    

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

@router.get("/predict_voltage/{soil_quantity}")
async def predict_voltage(soil_quantity: int):
    """
    Predict voltage based on soil quantity.

    Args:
        soil_quantity (int): The quantity of soil.

    Returns:
        dict: The predicted voltage.
    """
    return data_processing.voltage_calculation(soil_quantity)
