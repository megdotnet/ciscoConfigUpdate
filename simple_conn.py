#! python3
from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass
from global_var import *

ip_list = (path + folder + '\\ip_list.txt')

def connection(ip):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": cred_user,
        "password": getpass()
    }
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
    net_connect.disconnect()

#loop through the IP addresses in list.txt and test for connection
with open(ip_list) as f:
    lines = f.read().splitlines()
    for item in lines:
        ip = item.split(" ")[0]
        #print(ip)
        connection(ip)    