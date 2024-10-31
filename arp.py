#!/usr/bin/env python3
# Import scapy
import scapy.all as scapy
# We need to create regular expressions to ensure that the input is correctly formatted.
import re

# Basic user interface header
print(r"""WIFI SCANNER (ARP)""")
print("\n****************************************************************")

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Get the address range to ARP
while True:
    ip_add_range_entered = input("\nPlease enter the IP address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid IP address range")
        break

# Try ARPing the IP address range supplied by the user.
# The arping() method in scapy creates a packet with an ARP message
# and sends it to the broadcast MAC address ff:ff:ff:ff:ff:ff.
# If a valid IP address range was supplied, the program will return
# the list of all results.
arp_result = scapy.arping(ip_add_range_entered)
