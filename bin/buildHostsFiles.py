#!/usr/bin/env python
import sys
import subprocess
import os
import pprint
import glob

# Set current Working Directory
os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/../')
print "Current Working Directory: " + os.getcwd()	

# Cleanup old runs:
glob_dir = 'deploy/hosts/*'
glob_dir_files = glob.glob(glob_dir)
for file_name in glob_dir_files:
   os.remove(file_name)

# Get the names of the vagrant servers
command = "vagrant status | egrep --color=no '(digital_ocean)' | awk '{ print $1 }'"
servers_str = subprocess.check_output(command, shell=True).strip()

server_names = servers_str.split("\n")

server_ips = {}

for name in server_names:
	command = "vagrant ssh " + name + " -c \"ifconfig\" | grep inet | awk -F: '{ print $2 }' | awk '{ print $1 }' | grep --color=no \"^10\.\""
	ip = subprocess.check_output(command, shell=True).strip()
	server_ips[name] = ip

read_data = ""
with open('deploy/hosts_common', 'r') as f:
	read_data = f.read()
f.closed

# Write the hosts file

for name in server_names:
	if os.path.exists("deploy/hosts/" + name):
		os.remove("deploy/hosts/" + name)

	f = open("deploy/hosts/" + name, 'w')

	# Write the fully qualified domain
	f.write("127.0.0.1 " + name + " \n")
	f.write("127.0.1.1 " + name + " \n\n")

	for n in server_names:
		if n != name:
			f.write(server_ips[n] + " " + n + " \n")
	
	f.write("\n")

	f.write(read_data)

	f.close()

print "Finished!"