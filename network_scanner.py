#!/usr/bin/env python

import argparse
import re
import scapy.layers.l2 as l2
import scapy.all as scapy


def get_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--target", dest="target", help="Target you want to scan.")
  options = parser.parse_args()
  target_check = re.search(r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}($|/(3[0-2]|[1-2][0-9]|[0-9]))$", str(options.target))
  if not target_check:
    parser.error("Please specify a valid target IP address or IP range in CIDR notation, use --help or -h for information.")
  return options


def scan(ip):
  arp_request = l2.ARP(pdst=ip)
  broadcast = l2.Ether(dst="ff:ff:ff:ff:ff:ff")
  broadcast_arp_request = broadcast/arp_request
  answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
  clients_list = []
  for element in answered_list:
    clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
    clients_list.append(clients_dict)
  return clients_list


def print_result(results_list):
  print("IP\t\t\tMAC address\n-----------------------------------------")
  for client in results_list:
    print(client["ip"] + "\t\t" + client["mac"])
  
  
user_input = get_arguments()
scan_result = scan(user_input.target)
print_result(scan_result)
