import requests
import os
from time import time
from datetime import datetime, timezone
from dateutil import parser as date_parser
from modules import data_processing, post_data, notifications, alarms
from modules.database import db
from dotenv import load_dotenv

# Constants
# TELEGRAM_BOT_TOKEN = '7199765070:AAENYGOUL0XLq4CrwMfysoxM39Crgawi4ik'
# TELEGRAM_CHAT_ID = '-4205613285'

load_dotenv()
filtered_water_tds = os.getenv('filtered_water_tds')
unfiltered_water_tds = os.getenv('unfiltered_water_tds')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID =  os.getenv('TELEGRAM_CHAT_ID')

        # Check TDS value for specific nodes
tds_thresholds = {
    "WM-WD-KH98-00": float(unfiltered_water_tds),
    "WM-WD-KH96-00": float(unfiltered_water_tds),
    "WM-WD-KH96-01": float(unfiltered_water_tds),
    "WM-WD-KH04-00": float(filtered_water_tds),
    "WM-WD-KH03-00": float(filtered_water_tds),
    "WM-WD-KH95-00": float(filtered_water_tds)
    }

lower_threshold = 0

deadnode_check = {}

def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        if data['ok']:
            print(message)
        else:
            print('Failed to send Telegram notification')
    except requests.RequestException as e:
        print('Error sending Telegram notification:', e)

def parse_time(time_str):
    # Example: convert '15m' to milliseconds
    if time_str.endswith('m'):
        return int(time_str[:-1]) * 60 * 1000
    elif time_str.endswith('h'):
        return int(time_str[:-1]) * 60 * 60 * 1000
    # Add more cases as needed
    else:
        raise ValueError("Unsupported time format")

async def check_node_status(node_id, time_str, db):
    try:
        # Fetch node data
        data = data_processing.get_real_time_data(db, node_id)

        # Extract and convert timestamp to epoch
        timestamp = data['timestamp']
        if isinstance(timestamp, str):
            timestamp = date_parser.parse(timestamp).replace(tzinfo=timezone.utc).timestamp() * 1000
        elif isinstance(timestamp, datetime):
            timestamp = timestamp.replace(tzinfo=timezone.utc).timestamp() * 1000
        else:
            raise ValueError("Unsupported timestamp format")

        current_time = time() * 1000

        # Check if the timestamp is within the specified time range
        time_difference = current_time - timestamp
        time_limit = parse_time(time_str)

        if time_difference > time_limit:
            message = f"Node {node_id} is down!"
            print(message)
            alarm_data = {'node_id': node_id, 'alarm_type': 'down', 'alarm_value': message}
            send_telegram_notification(message)
            alarms.insert_alarm(db, alarm_data)
            # Increase the value of the node_id in deadnode_check dictionary
            deadnode_check[node_id] = deadnode_check.get(node_id, 0) + 1

        if node_id in tds_thresholds:
            tds_value = data.get('compensated_tds')
            if tds_value is not None:
                if tds_value > tds_thresholds[node_id]:
                    tds_alert_message = f"Alert! Node {node_id} TDS value is {tds_value} (exceeds threshold)"
                    notification_data = {'node_id': node_id, 'notification_type': 'threshould','notification_value': tds_alert_message}
                    notifications.insert_notification(db, notification_data)
                    send_telegram_notification(tds_alert_message)
                    
                elif tds_value < lower_threshold:
                    tds_alert_message = f"Alert! Node {node_id} TDS value is negitive: {tds_value}"
                    notification_data = {'node_id': node_id, 'notification_type': 'negitive','notification_value': tds_alert_message}
                    notifications.insert_notification(db, notification_data)
                    # Increase the value of the node_id in since value is negitive
                    deadnode_check[node_id] = deadnode_check.get(node_id, 0) + 1
                    send_telegram_notification(tds_alert_message)
                    
        
        #Adding the node_id to the dictionary if it is not present
        deadnode_check[node_id] = deadnode_check.get(node_id, 0) + 0
        # Check if the value exceeds 6
        if deadnode_check[node_id] > 6:
            # Reset the value to 0
            deadnode_check[node_id] = 0
                
            # Send notification to Telegram
            message = f"Node {node_id} is down for the last 3 hours. Resetting the node."
            print(message)
            send_telegram_notification(message)
            post_data.post_to_onem2m_act(node_id, 1)
            message = f"Node {node_id} is reset."
            print(message)
            send_telegram_notification(message)
            
        return True

    except requests.RequestException as e:
        print(f"Fetch error for {node_id}: {e}")