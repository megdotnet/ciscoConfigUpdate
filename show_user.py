#! python3

from global_var import *

print("\n Enter credentials for. " + folder)
cred_user = input("login as: ")
cred_pass = getpass()

def config(ip):
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": cred_user,
    "password": cred_pass,
    }

    try:
        with ConnectHandler(**device) as net_connect:
            lines = net_connect.send_command("show run").splitlines() 
            hostname=get_hostname(lines)
            print("----[ " + hostname + "  " + ip + " ]----")
            for item in lines:
                if "user" in item:
                    print(item)
            print("\n")
    except:
        print("An Error Ocurred connecting to " + ip + ".")
        
with open(ip_list) as f:
    lines = f.read().splitlines()
    for item in lines:
        ip = item.split(" ")[1]
        config(ip)       
        
