from ncclient import manager
# import logging
import xmltodict

# logging.basicConfig(level=logging.DEBUG)

router = {
    "host": "192.168.2.11",
    "port":     830,
    "username": "okan",
    "password": "hollander"
}

int_filter = """
    <filter>
      <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
        <interface>
          <name>GigabitEthernet2</name>
          <interface-type/>
          <speed/>
          <ipv4/>
        </interface>
      </interfaces>
    </filter>
"""

with manager.connect(**router, hostkey_verify=False) as m:
    netconf_response = m.get(int_filter)

python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
op = python_response["interfaces-state"]["interface"]
config = python_response["interfaces"]["interface"]

print(f"Name: {config['name']['#text']}")
print(f"Packets In: {op['statistics']['in-unicast-pkts']}")