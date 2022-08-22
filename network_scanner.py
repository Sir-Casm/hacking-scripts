#!/usr/bin/env python

import scapy.layers.l2 as l2
import scapy.all as scapy


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
  
  
scan_result = scan("10.0.2.1/24")
print_result(scan_result)
