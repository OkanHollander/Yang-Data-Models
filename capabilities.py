from ncclient import manager

router = {
    "host": "192.168.2.11",
    "port": "830",
    "username": "okan",
    "password": "hollander"
}

with manager.connect(**router, hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print("*" * 25)
        print(' ')
        print(capability)

