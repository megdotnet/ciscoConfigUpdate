#! python3
from netmiko import Netmiko
from credentials import cred_user,cred_pass
from netmiko import ConnectHandler

def connection(ip):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": cred_user,
        "password": cred_pass,
    }
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()

#loop through the IP addresses in list.txt and test for connection
with open('D:\\OneDrive - Tacocat\\Code\\git\\ciscoConfigUpdate\\list.txt') as f:
    lines = f.read().splitlines()
    for ip in lines:
        connection(ip)    