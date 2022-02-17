#! python3

import os, re, shutil
from global_var import *
from pythonping import ping
from pythonping.executor import Response

def parse(fullname):
    ping_success=False
    with open(cfg_path) as fp:
        try:
            lines = fp.read().splitlines()
            hostname = get_hostname(lines)

            ip_addresses = [
            line.split(" ")[3]
            for line in lines
            if "ip address" in line.strip() and
            line.strip() != "no ip address" and 
            "10.1.1.1" not in line.strip() and 
            "match" not in line.strip()
            ]

            for ip_addr in ip_addresses:
                print("----------")
                print("Pinging: " + hostname + " at " + ip_addr)
                for c in range(4):
                    response_list = ping(ip_addr, timeout=1, count=1)
                    print(str(response_list._responses[0]))
                    if ("Reply from " + ip_addr) in str(response_list._responses[0]):
                        print("Pinging " + hostname + " at " + ip_addr + " successful.")
                        print("Added to " + ip_list)
                        ping_success=True
                        break
                if ping_success:
                    break 
            
            file = open(ip_list, "a")                        
            if ping_success!=True:
                print("Pinging " + hostname + " failed.")
                file.write(hostname + ",[ping failed] \n")
            else: 
                file.write(hostname + "," + ip_addr + "\n")
            file.close()    
        
        except: 
            print('Error reading ' + fullname)
            file = open(ip_list, "a")                        
            file.write('Error reading ' + fullname + "\n")
        
#read each file in the directory


if folder_confirm():
    os.chdir(project_path)

    file = open(ip_list, "w")
    file.write("Hostname,IP Address\n")
    file.close()

    for name in os.listdir():
        if name.endswith('.cfg'):
            cfg_path = project_path + "\\" + name
            parse(cfg_path)    

else:
    print("Exiting")

