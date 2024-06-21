import requests
from time import time
from datetime import datetime, timezone
from dateutil import parser as date_parser
from modules import data_processing

# Constants
BACKEND_API = "http://smartcitylivinglab.iiit.ac.in:1629"
TELEGRAM_BOT_TOKEN = '7199765070:AAENYGOUL0XLq4CrwMfysoxM39Crgawi4ik'
TELEGRAM_CHAT_ID = '-4205613285'

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
            print('Telegram notification sent successfully:', data)
        else:
            print('Failed to send Telegram notification:', data)
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
        
        print(f"Node {node_id} data:")
        for key, value in data.items():
            print(f"{key}: {value}")

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
            send_telegram_notification(message)

        # Check TDS value for specific nodes
        tds_thresholds = {
            "WM-WD-KH98-00": 500,
            "WM-WD-KH96-00": 500,
            "WM-WD-KH04-00": 150,
            "WM-WD-KH95-00": 150
        }

        lower_threshold = 50

        if node_id in tds_thresholds:
            tds_value = data.get('compensated_tds')
            if tds_value is not None:
                if tds_value > tds_thresholds[node_id]:
                    tds_alert_message = f"Alert! Node {node_id} TDS value is {tds_value} (exceeds threshold)"
                    print(tds_alert_message)
                    send_telegram_notification(tds_alert_message)
                elif tds_value < lower_threshold:
                    tds_alert_message = f"Alert! Node {node_id} TDS value is {tds_value} (below lower threshold)"
                    print(tds_alert_message)
                    send_telegram_notification(tds_alert_message)
        return True

    except requests.RequestException as e:
        print(f"Fetch error for {node_id}: {e}")