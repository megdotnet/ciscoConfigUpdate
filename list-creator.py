#! python3

import os, re, shutil

#user defined variables
search= "ip address 10.11."
folder = "TCORE"

path = ('C:\\users\\fairbanksm\\OneDrive - Tacocat\\Code\\git\\ciscoConfigUpdate\\' + folder)
outpath = path + "\\ip_list.txt"

os.chdir(path)

file = open(outpath, "w")
file.close()

#find the first ip address that mathes search and stop
def parse(fullname):
    with open(fullpath) as fp:
        lines = fp.read().splitlines()
        for line in lines:
            if "hostname" in line.strip(): 
                hostname = line.split(" ")[1]
            if search in line.strip():
                nat_rules = line.split(" ")[3]
                file = open(outpath, "a")
                file.write(nat_rules + " " + hostname + "\n")
                file.close()
                break

#read each file in the directory
for name in os.listdir():
    if name.endswith('.cfg'):
        fullpath = path + "\\" + name
        parse(fullpath)




