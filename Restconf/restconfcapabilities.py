import requests
import json

router = {
    "host": "192.168.2.11",
    "port": "443",
    "user": "okan",
    "password": "hollander"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"


headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

response = requests.get(url=url, 
                       headers=headers, 
                       auth=(router['user'],router['password']), 
                       verify=False)

if response.status_code == 200:
    response_dict = response.json()
    for cap in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
        print(cap)