#! python3

from global_var import *

cred_pass = getpass()

def connection(ip, cred_pass):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": cred_user,
        "password": cred_pass
    }
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()

#loop through the IP addresses in list.txt and test for connection
with open(ip_list) as f:
    lines = f.read().splitlines()
    for item in lines:
        ip = item.split(" ")[1]
        connection(ip,cred_pass)   
        print(ip)