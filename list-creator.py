#! python3

import os, re, shutil

search= "ip address 10.201."
folder = "DFW"

path = ('D:\\OneDrive - Tacocat\\Code\Cisco Python\\' + folder)
outpath = path + "\\ip_list.txt"

os.chdir(path)

file1 = open(outpath, "w")
file1.close()

def parse(fullname):
    with open(fullpath) as fp:
        lines = fp.read().splitlines()
        for line in lines:
            if search in line.strip():
                nat_rules = line.split(" ")[3]
                file1 = open(outpath, "a")
                file1.write(nat_rules + "\n")
                file1.close()
                break

#read each file in the directory
for name in os.listdir():
    if name.endswith('.cfg'):
        fullpath = path + "\\" + name
        parse(fullpath)




