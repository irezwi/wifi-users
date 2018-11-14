import os
import re

# Dict with addresses to find
persons = {
    'AA:BB:CC:DD:EE:FF': 'John Doe',
}

# Get user local IP address
hostname_response = os.popen('hostname -I').read().split('.')
hostname_response[-1] = '0'
hostname_response = '.'.join(hostname_response)

# Remove empty lines and spaces
user_local_ip = "".join(hostname_response).replace('\n', '').replace(' ', '')

# Searching for MAC addresses in arp-scan request
arp_out = " ".join(os.popen('sudo -S arp-scan ' + user_local_ip + '/25 ' + '-g').readlines())
mac_addresses = re.findall(r'(?:[0-9a-fA-F]:?){12}', arp_out)

# Printing found addresses
for address in mac_addresses:
    if address in persons.keys():
        print("Address {} matched as {}".format(address, persons[address]))
    else:
        print("Address {} not matched.".format(address))
