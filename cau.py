#! /usr/bin/env python

#An application to update Access Control Lists (ACLs) on Cisco IOS routers

from netmiko import ConnectHandler

print("-" * 30)
print("      ACL updater")
print("-" * 30)

router_name = input("What is the name of the router? ")
acl_name = input("What is the name of the ACL? ")

print("Grabbing current ACL from", router_name)

device_connect = {
    'device_type': 'cisco_ios',
    'host': router_name,
    'username': 'username',
    'password': 'password',
}
net_connect = ConnectHandler(**device_connect)
command = "show run | sec ip access-list extended {}".format(acl_name)

print("The current", acl_name, "ACL on router", router_name,":")
print(net_connect.find_prompt())
output = net_connect.send_command(command)
net_connect.disconnect()
print(output)
print()

#with the ACL stored as "output" write the ACL to a file called acl.txt and file called new_acl.txt
with open ("acl.txt", "w") as f:
    f.write(output)

with open ("new_acl.txt", "w") as f:
    f.write(output)


#prompt the user for the details of the new port to open
protocol = input("What is the protocol ?")
port_number = input("What is the port number? ")
destination = input("what is the destination? ")


ace = ' permit ' + protocol + ' any ' + destination + ' eq ' + port_number + '\n'

#open the file new_acl.txt and read the contents into the "contents" variable, then insert the new ACE at line 1
#write the file again with the joined contents

with open("new_acl.txt", "r") as f:
    contents = f.readlines()
    contents.insert(1, str(ace))

with open("new_acl.txt", "w") as f:
    contents = "".join(contents)
    f.write(contents)
