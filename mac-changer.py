#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface you want to change the MAC address for.")
parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address you want to set.")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
