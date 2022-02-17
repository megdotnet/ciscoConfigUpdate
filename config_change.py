#! python3

from global_var import *
import re

cred_user = input("login as: ")
cred_pass = getpass()

#user defined variables
new_tftp_server = ""
old_tftp_server = ""

#open the log file for writing (new blank file)
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
        try:
            #open the log file for writing (append)
            file = open(ip_log, "a")
            
            #get the hostname
            output = net_connect.send_command("show run | inc hostname")
            hostname = output[9:]
            print(hostname)
            file.write("   Hostname: " + hostname + "\n")
            
            #get the current cli command
            output = net_connect.send_command("show run | inc cli")
            file.write("Current Cli: " + output.strip())
            
            #check for new server first
            if new_tftp_server in output: 
                print("New TFTP server already in config.")
                file.write("    Message: New TFTP server already in config. \n")
            
            #delete old server and add new
            else:
                #put 'no' in front of the existing cli command
                no_cli = "no" + output
                #create new backup command
                backup = "show run | redirect tftp://" + new_tftp_server + "/" + folder + "/" + hostname + ".cfg"
                file.write("    Backup : " + backup + "\n")
                #create new cli command
                new_cli = "cli " + backup
                file.write("   New cli : " + new_cli + "\n")
                #send the new commands
                kron = "kron policy-list Backup"
                output = net_connect.send_config_set([kron, no_cli, new_cli])
                print(output)
                file.write(output)
                #run manual backup now
                output = net_connect.send_command(backup)
                print("[manual backup] " + backup + "\n")
                file.write("Manual Bkup: " + backup + "\n")
                #save config              
                output = net_connect.save_config()
                print(output)
                file.write(output + "\n")
            
            print("-----")
            file.write("----- \n")
            file.close()
            
        except:
            print("An Error Ocurred")
            file.write("----- \n")
            file.close()
            

with open(ip_list) as f:
    lines = f.read().splitlines()
    for item in lines:
        ip = item.split(" ")[1]
        config(ip)       
        
