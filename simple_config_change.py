#! python3
from netmiko import Netmiko
from netmiko import ConnectHandler


tftp_server = "10.11.16.27"
folder="TCORE"


def config(ip):
    device = {
    "device_type": "cisco_ios",
    "host": ip,
    "username": "fairbanksm",
    "password": "Sch@ffer42",
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

with open('D:\\OneDrive - Tacocat\\Code\Cisco Python\\list.txt') as f:
    lines = f.read().splitlines()
    for ip in lines:
        config(ip)
