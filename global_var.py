#! python3
from getpass import getpass
from netmiko import ConnectHandler
import os

#FEY
#path = "D:\\OneDrive - Tacocat\\Code\\ciscoConfigUpdate\\"

#FAIRBANKSM3  
#path = ('C:\\users\\fairbanksm\\OneDrive - Tacocat\\Code\\ciscoConfigUpdate\\')

#onedrive_path = os.environ.get('onedrive')
#print(onedrive_path)

path = (os.environ.get('onedrive') + "\\code\\ciscoConfigUpdate\\")

cred_user="tcore"
folder="TCORE"
project_path = (path + folder)
ip_list = (project_path + "\\ip_list.txt")
ip_log = (project_path + "\\ip_log.txt")


