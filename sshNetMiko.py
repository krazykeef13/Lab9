import os
from netmiko import ConnectHandler
from getpass import getpass


USERNAME = input("Please enter your username: ")
PASS = getpass("Please enter your password: ")

device = {
    'host': '192.168.44.3',
    'username': 'USERNAME',
    'password': 'PASS',
    'device_type': 'cisco_ios'
}

c = ConnectHandler(**device)

output = c.send_command('show run')

f = open('backup.conf', 'x')

f.write(output)
f.close()
