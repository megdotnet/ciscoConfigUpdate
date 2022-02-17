#! python3

from getpass import getpass
from netmiko import ConnectHandler
import sys
import os

ip=sys.argv[1]

cred_user = input("login as: ")
cred_pass = getpass()

def connect(ip):
    
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": cred_user,
    "password": cred_pass,
    }
    
    with ConnectHandler(**device) as net_connect:
        line = net_connect.send_command("show run | inc hostname")
        #hostname = line.split(" ")[1]
        print(line)


connect(ip)     
