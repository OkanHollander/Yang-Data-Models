import requests
import json

router = {
    "host": "192.168.2.11",
    "port": "443",
    "username": "okan",
    "password": "hollander"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(url=url, 
                       headers=headers, 
                       auth=(router['username'], router['password']),
                       verify=False).json()

print(json.dumps(response, indent=2))