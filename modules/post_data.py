import json
import requests

BACKEND_URL="http://onem2m.iiit.ac.in:443/~/in-cse/AE-DM/"

def post_to_onem2m(NodeID,data):
    url = BACKEND_URL+NodeID+"/Control"
    data = str(data)
    data_json = json.dumps(data)
    payload = json.dumps({
        "m2m:cin": {
            "con": data
        }
    })
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Content-Type': 'application/json;ty=4'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)