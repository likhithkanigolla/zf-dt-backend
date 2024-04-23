import json
import requests
import time

BACKEND_URL="http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-DM/"

def post_to_onem2m_act(node_type, node_name, status):
    epoch_time = int(time.time())
    data_list = [epoch_time,node_type,status]  # Initialize the data list with some default values
    url = BACKEND_URL + node_name + "/Control"
    data_list=str(data_list)
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
    return response.text