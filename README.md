ARP Scanner
A Python script for scanning a local network using ARP (Address Resolution Protocol) requests to identify active devices. This script uses Scapy to send ARP requests over the network and gather the IP and MAC addresses of devices in a specified IP range.

Table of Contents
Introduction
Features
Requirements
Usage
Installation

Introduction
This tool performs an ARP scan on a specified IP address range and displays the IP and MAC addresses of devices that respond. It is helpful for identifying devices in a local network.

Features
Simple command-line interface.
Customizable IP address range.
Displays valid IP address ranges and only proceeds if a valid range is entered.
Requirements
Python 3.x
Scapy library (for packet crafting and network communication)
Installation:
Clone the repository:
git clone https://github.com/YOUR_USERNAME/ARP-Scanner.git
cd ARP-Scanner
Usage
Run the script with the following command:
python3 arp_scanner.py

credits: https://github.com/davidbombal/red-python-scripts/blob/main/lanscan_arp.py
