#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface you want to change the MAC address for.")
  parser.add_option("-m", "--mac", dest="new_mac", help="The new MAC address you want to set.")
  (options, arguments) = parser.parse_args()
  if not options.interface:
    parser.error("Please specify an interface, use --help or -h for information.")
  mac_check = re.search(r"^((([a-f0-9]{2}:){5})|(([a-f0-9]{2}-){5}))[a-f0-9]{2}$", options.new_mac)
  if not mac_check:
      parser.error("Please specify a valid new MAC address for the target interface, use --help or -h for information.")
  return options


def change_mac(interface, new_mac):
  print("Changing MAC address for " + interface + " to " + new_mac)
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
  subprocess.call(["ifconfig", interface, "up"])

  
def get_current_mac(interface):
  interface_check = subprocess.check_output(["ifconfig", interface])
  mac_check = re.search(r"((([a-f0-9]{2}:){5})|(([a-f0-9]{2}-){5}))[a-f0-9]{2}", interface_check)
  if mac_check:
    return mac_check.group(0)
  else:
    print("Could not read the MAC address.")


options = get_arguments()

current_mac = get_current_mac(options.interface) 
print("Current MAC address: " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
  print("The MAC address was successfully changed to: " + current_mac)
else:
  print("The MAC address did not change.")
