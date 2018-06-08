import os
import re

# Dict with addresses to find
persons = {'AA:BB:CC:DD:EE:FF': 'John Doe'}

# Searching for MAC addresses in arp-scan request
arp_out = " ".join(os.popen('sudo arp-scan 192.168.1.0/24 -g').readlines())
mac_addresses = re.findall(r'(?:[0-9a-fA-F]:?){12}', arp_out)

# Printing found addresses
for address in mac_addresses:
    if address in persons.keys():
        print("Address {} matched as {}".format(address, persons[address]))
    else:
        print("Address {} not matched.".format(address))
