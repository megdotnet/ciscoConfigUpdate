#! python3

from global_var import *
from getpass import getpass

def connection(ip, hostname):
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": cred_user,
        "password": cred_pass
    }
           
    try: 
        net_connect = ConnectHandler(**device)
        print(net_connect.find_prompt())
        net_connect.disconnect()
        print("Connection to " + ip + " successful")
        file = open(ip_conn, "a") 
        file.write(hostname + "," + ip + "," + cred_user + ",success\n")
        file.close()            
    
    except:
        print("Error connecting to " + hostname + " at "+ ip)
        file = open(ip_conn, "a") 
        file.write(hostname + "," + ip + "," + cred_user + ",fail\n")
        file.close()            
        
    print("----------")

        
#loop through the IP addresses in list.txt and test for connection
print("\n       Protocol: SSH")
if folder_confirm():
    os.chdir(project_path)

    file = open(ip_conn, "w")
    file.write("Hostname,IP Address,Username,Connection\n")
    file.close()

    print("\n Enter credentials for: " + folder)
    cred_user = input("login as: ")
    cred_pass = getpass()

    with open(ip_list) as f:
        lines = f.read().splitlines()
        for item in lines:
            if "Error" not in item and "failed" not in item and "Hostname" not in item:
                hostname = item.split(",")[0]
                ip = item.split(",")[1]
                connection(ip, hostname)       
    
else:
    print("Exiting")




