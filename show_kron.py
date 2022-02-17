#! python3

from global_var import *

cred_user = input("login as: ")
cred_pass = getpass()

file = open(ip_confirm, "w")
file.close()


def get_kron(lines):
    for item in lines:
        if ("kron occurrence") in item: 
            out_log(item,ip_confirm)
        if ("policy-list") in item: 
            out_log(item,ip_confirm)
        if ("cli ") in item: 
            out_log(item,ip_confirm)

def config(ip):
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": cred_user,
    "password": cred_pass,
    "secret" : "",
    "session_log": "c:\\netmiko_session.log"
    }
    
    file = open(ip_confirm, "a")
            
    try:
        with ConnectHandler(**device) as net_connect:
            print("Connecting to: " + ip)
            net_connect.enable()
            lines = net_connect.send_command("show run").splitlines() 
            hostname=get_hostname(lines)
            print("Hostname: " + hostname)
            out_log("----[ " + hostname + "  " + ip + " ]----",ip_confirm)
            get_kron(lines)
            out_log("\n",ip_confirm)
            
    except:
        print("An error ocurred")
        file.write("An error ocurred")

    file.close()

with open(ip_list) as f:
    lines = f.read().splitlines()
    for item in lines:
        ip = item.split(" ")[1]
        config(ip)       
        
