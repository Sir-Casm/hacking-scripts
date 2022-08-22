#!/usr/bin/env python

import subprocess


interface = input("Choose a network interface: ")
new_mac = input("Choose a new MAC address: ")

print("Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
