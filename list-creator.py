#! python3

import os, re, shutil
from global_var import *
from pythonping import ping
from pythonping.executor import Response, SuccessOn

os.chdir(project_path)

file = open(ip_list, "w")
file.close()

#find the first ip address pings and stop
def parse(fullname):
    ping_success=False
    with open(cfg_path) as fp:
        lines = fp.read().splitlines()
        for line in lines:
            if "hostname" in line.strip(): 
                hostname = line.split(" ")[1]
                break
        for line in lines:
            if "ip address" in line.strip():
                ip_addr = line.split(" ")[3]
                #file = open(ip_list, "a")
                #file.write(nat_rules + " " + hostname + "\n")
                #file.close()
                if line.strip() != "no ip address" and ip_addr!="10.1.1.1":
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
                    if ping_success==True:
                        break 
    
    file = open(ip_list, "a")                        
    if ping_success!=True:
        print("Pinging " + hostname + " failed.")
        file.write(hostname + " [ping failed] \n")
    else: 
        file.write(hostname + " " + ip_addr + "\n")
    file.close()
                                
#read each file in the directory
for name in os.listdir():
    if name.endswith('.cfg'):
        cfg_path = project_path + "\\" + name
        parse(cfg_path)




