#! python3

from getpass import getpass
from netmiko import ConnectHandler
import os


folder=""

path = ("C:\\TFTP-Root\\")

project_path = (path + folder)
ip_list = (project_path + "\\_ip_list.csv")
ip_log = (project_path + "\\_ip_log.txt")
ip_confirm = (project_path + "\\_show_kron.txt")
ip_conn = (project_path + "\\_ip_conn.csv")
ip_kron = (project_path + "\\_ip_kron.csv")

def folder_confirm():
    print(" Current folder: " + project_path)
    reply = input("(y) to continue: ")
    if reply == 'y' or reply == "Y":
        return True

def get_hostname(lines):
    for item in lines:
        if "hostname" in item.strip(): 
            hostname = str(item.split(" ")[1])
            return hostname

def out_log(message,out_path):
    file = open(out_path, "a")
    print(message)
    file.write(message + "\n")
