#! python3

import os, re, shutil

search= "ip address 10.11."
folder = "TCORE"

path = ('D:\\OneDrive - Tacocat\\Code\\git\\ciscoConfigUpdate\\' + folder)
outpath1 = path + "\\ip_list.txt"
outpath2 = path + "\\ip_hostname_list.txt"

os.chdir(path)

file1 = open(outpath1, "w")
file2 = open(outpath2, "w")
file1.close()
file2.close()

#find the first ip address that mathes search and stop
def parse(fullname):
    with open(fullpath) as fp:
        lines = fp.read().splitlines()
        for line in lines:
            if "hostname" in line.strip(): 
                hostname = line.split(" ")[1]
            if search in line.strip():
                nat_rules = line.split(" ")[3]
                file1 = open(outpath1, "a")
                file1.write(nat_rules + "\n")
                file1.close()
                file2 = open(outpath2, "a")
                file2.write(nat_rules + " " + hostname + "\n")
                file2.close()
                break

#read each file in the directory
for name in os.listdir():
    if name.endswith('.cfg'):
        fullpath = path + "\\" + name
        parse(fullpath)




