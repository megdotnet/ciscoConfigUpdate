#! python3

import os
from pythonping import ping
from pythonping.executor import Response, SuccessOn

hostname = "HOU-FAKE-HOST"
host = "8.8.8.55"

def ping_test(ip_addr):
    print("Pinging: " + hostname + " at " + ip_addr)
    for c in range(4):
        response_list = ping(host, timeout=1, count=1)
        print(str(response_list._responses[0]))
        if ("Reply from " + ip_addr) in str(response_list._responses[0]):
            print("Pinging " + hostname + " at " + ip_addr + " successful.")
            print(hostname + " added to ip_list.tst")
            
                
ping_test(host)