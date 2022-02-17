#! python3

from os import terminal_size
from global_var import *
import re

#user defined variables
path = "" + folder + "/$h_"
archive = ["archive", path, "write-memory"]

kron = "kron policy-list Backup" 
new_cli = "cli write memory"
commands = [kron, new_cli] 

def test_new_cli(output):
    for line in output.splitlines():
        if new_cli in line:
            return True
        else: 
            return False

def config(hostname, ip):
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": cred_user,
    "password": cred_pass,
    }

    with ConnectHandler(**device) as net_connect:
        try:
            #open the log file for writing (append)
            file = open(ip_log, "a")
                    
            #send the archive settings (it's okay to overwrite if they already exist)
            print("Connecting to " + hostname + " at " + ip)
            output = net_connect.send_config_set(archive)
            file.write("-----  " + hostname + " at " + ip + "  -----\n")
            file.write(output + "\n")
            
            #get the current cli command(s)
            output = net_connect.send_command("show run | inc " + new_cli)
            if test_new_cli(output):
                print("New CLI job already exists")
            else:
                output = net_connect.send_config_set(commands)
                file.write(output + "\n")
                
            #save config              
            output = net_connect.save_config()
            file.write(output + "\n")
            print("Done")
        
        except:
            print("An Error Ocurred")
            file.write("An Error Ocurred\n")
            
        #close the file
        print("-----")
        file.write("-----  END  -----\n\n")
        file.close()
 
if folder_confirm():
    #credentials
    print("\n Enter credentials for: " + folder)
    cred_user = input("login as: ")
    cred_pass = getpass()
    
    #open the log file for writing (new blank file)
    file = open(ip_log, "w")
    file.close()

    
    with open(ip_conn) as f:
        lines = f.read().splitlines()
        for item in lines:
            if "Hostname" not in item and "fail" not in item:
                hostname = item.split(",")[0]
                ip = item.split(",")[1]
                config(hostname, ip)

else:
    print("Exiting")