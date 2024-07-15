import json
import requests
import time
import os
import re
from dotenv import load_dotenv

load_dotenv()
threshold = os.getenv('WM-WD-KH95-00')
print(threshold)

BACKEND_URL = "http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-DM/"

# Dictionary mapping patterns to container names
pattern_to_container = {
    re.compile(r'.*-.*-KH98-.*'): 'DM-KH98-80',
    re.compile(r'.*-.*-KH95-.*'): 'DM-KH95-80',
    re.compile(r'.*-.*-KH96-.*|.*-.*-KB04-.*|.*-.*-KH00-.*'): 'DM-KH96-80',
    re.compile(r'.*-.*-KH03-.*'): 'DM-KH03-80'
}

def get_container_name(node_name):
    for pattern, container_name in pattern_to_container.items():
        if re.match(pattern, node_name):
            return container_name
    return "No matching container found"

def post_to_onem2m_act(node_name, status):
    container_name = get_container_name(node_name)
    if container_name == "No matching container found":
        print(f"No matching container found for node name: {node_name}")
        return

    epoch_time = int(time.time())
    data_list = [epoch_time, node_name, status]  # Initialize the data list with some default values
    url = BACKEND_URL + container_name + "/Control"
    # print(url)
    data_list = str(data_list)
    payload = json.dumps({
        "m2m:cin": {
            "con": data_list
        }
    })
    headers = {
        'X-M2M-Origin': 'DeviceMon@20:9G&6OnuL1iZ',
        'Content-Type': 'application/json;ty=4'
    }
    response = requests.post(url, headers=headers, data=payload)
    print("Response Code: ", response.status_code)
    return response.status_code
