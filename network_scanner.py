#!/usr/bin/env python

import scapy.layers.l2 as l2
import scapy.all as scapy


def scan(ip):
  arp_request = l2.ARP(pdst=ip)
  broadcast = l2.Ether(dst="ff:ff:ff:ff:ff:ff")
  broadcast_arp_request = broadcast/arp_request
  answered_list, unanswered_list = scapy.srp(broadcast_arp_request, timeout=1)
  print(answered_list.summary())
  
  
scan("10.0.2.1/24")
