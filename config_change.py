#! python3

from global_var import *

cred_pass = getpass()

#user defined variables
tftp_server = "10.11.192.27"

file = open(ip_log, "w")
file.close()

def config(ip):
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": cred_user,
    "password": cred_pass,
    }

    with ConnectHandler(**device) as net_connect:
        file = open(ip_log, "a")
        #get the hostname
        output = net_connect.send_command("show run | inc hostname")
        hostname = output[9:]
        print(hostname)
        file.write(hostname + "\n")
        #get the current cli command and negate
        output = net_connect.send_command("show run | inc cli")    
        no_cli = "no" + output
        #create new backup command
        backup = "show run | redirect tftp://" + tftp_server + "/" + folder + "/" + hostname + ".cfg"
        #create new cli command
        new_cli = "cli " + backup
        #kill the old backup job and add the new one
        kron = "kron policy-list Backup"
        output = net_connect.send_config_set([kron, no_cli, new_cli])
        print(output)
        file.write(output)
        #run manual backup now
        output = net_connect.send_command(backup)
        print("[manual backup] " + backup + "\n")
        file.write("[manual backup] " + backup + "\n")
        #save config              
        output = net_connect.save_config()
        print(output)
        print("-----")
        file.write(output + "\n")
        file.write("----- \n")
        file.close()

with open(ip_list) as f:
    lines = f.read().splitlines()
    for item in lines:
        ip = item.split(" ")[1]
        config(ip)       
        