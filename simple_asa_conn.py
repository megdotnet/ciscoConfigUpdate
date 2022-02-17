#! python3

from global_var import *
from getpass import getpass

ip = ""

cred_user = input("login as: ")
cred_pass = getpass()

def connection(ip):
    device = {
        "device_type": "cisco_asa_ssh",
        "host": ip,
        "username": cred_user,
        "password": cred_pass
    }
    try: 
        net_connect = ConnectHandler(**device)
        print(net_connect.find_prompt())
        net_connect.disconnect()
        
    except:
        print("Error connecting to " + ip)
    
    

    
    
    

connection(ip)
