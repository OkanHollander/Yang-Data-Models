from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "192.168.2.11",
    "auth_username": "okan",
    "auth_password": "hollander",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfDriver(**my_device)
conn.open()

rpc_filter = '''
<get>
<filter xmlns:t="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper" type="xpath" select="/ospf-oper-data/ospf-state/ospf-instance[af='address-family-ipv4' and router-id='16843009']/ospf-area[area-id=0]/ospf-interface[name='GigabitEthernet2']/ospf-neighbor[neighbor-id='2.2.2.2']/state" />
</get>
'''

response = conn.rpc(rpc_filter)
print(response.result)