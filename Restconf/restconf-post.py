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

url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces"


payload = {
  "ietf-interfaces:interface":{
        "name": "Loopback100",
        "description": "INTERFACE RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "172.16.100.1",
              "netmask": "255.255.255.0"
            }
          ]
        }
    }
}

response = requests.post(url=url,
                         headers=headers,
                         auth=(router["username"], router["password"]),
                         verify=False,
                         data=json.dumps(payload))

if response.status_code == 201:
    print(response.text)
print(response.text)