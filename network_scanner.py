#!/usr/bin/env python

import scapy.layers.l2 as l2
import scapy.all as scapy


def scan(ip):
  arp_request = l2.ARP(pdst=ip)
  broadcast = l2.Ether(dst="ff:ff:ff:ff:ff:ff")
  broadcast_arp_request = broadcast/arp_request
  answered_list = scapy.srp(broadcast_arp_request, timeout=1)[0]
  for element in answered_list:
    print(element)
    print("---------------")
  
  
scan("10.0.2.1/24")
