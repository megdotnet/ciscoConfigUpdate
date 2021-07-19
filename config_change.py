#! python3
from netmiko import Netmiko
from netmiko import ConnectHandler
from credentials import cred_user,cred_pass

#user defined variables
tftp_server = "10.11.16.27"
folder="TCORE"

path = ('D:\\OneDrive - Tacocat\\Code\\git\\ciscoConfigUpdate\\')
ip_list = ('D:\\OneDrive - Tacocat\\Code\\git\\ciscoConfigUpdate\\' + folder + '\\ip_list.txt')
outpath = path + "\\ip_log.txt"

file = open(outpath, "w")
file.close()

def config(ip):
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": cred_user,
    "password": cred_pass,
    }

    with ConnectHandler(**device) as net_connect:
        #get the hostname
        output = net_connect.send_command("show run | inc hostname")
        hostname = output[9:]
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
        #run manual backup now
        net_connect.send_command(backup)
        #save config              
        output += net_connect.save_config()

    print()
    print(output)
    print()
    file = open(outpath, "a")
    file.write(output + "\n")
    file.close()

with open(ip_list) as f:
    lines = f.read().splitlines()
    for ip in lines:
        config(ip)       
        