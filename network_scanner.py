#!/usr/bin/env python

import scapy.layers.l2 as l2


def scan(ip):
  arp_request = l2.ARP(pdst=ip)
  broadcast = l2.Ether(dst="ff:ff:ff:ff:ff:ff")
  broadcast_arp_request = broadcast/arp_request
  print(broadcast_arp_request.summary())
  print(broadcast_arp_request.show())
  
  
scan("10.0.2.1/24")
