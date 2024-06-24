import json
import requests
import time
import os
from dotenv import load_dotenv
# from config.settings import *

load_dotenv()
threshold = os.getenv('WM-WD-KH95-00')
print(threshold)

BACKEND_URL="http://onem2m.iiit.ac.in:443/~/in-cse/in-name/AE-DM/"

def post_to_onem2m_act(node_name, status):
    epoch_time = int(time.time())
    data_list = [epoch_time,node_name,status]  # Initialize the data list with some default values
    # url = BACKEND_URL + node_name + "/Control"
    url = BACKEND_URL + "DM-KH98-80" + "/Control"
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
    print("Response Code: ",response.status_code)
    return response.status_code
# print(DATABASE_URL)