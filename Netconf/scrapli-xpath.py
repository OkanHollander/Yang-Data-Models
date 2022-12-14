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

ospf_xpath = '/ospf-oper-data/ospf-state/ospf-instance[af="address-family-ipv4" and router-id="16843009"]/ospf-area[area-id=0]/ospf-interface[name="GigabitEthernet2"]/ospf-neighbor[neighbor-id="2.2.2.2"]/state'
response = conn.get(
    filter_=ospf_xpath, filter_type='xpath')
print(response.result)