#!/usr/bin/env python

import netfilterqueue
import scapy.layers.inet as inet
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = inet.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[inet.TCP].dport == 80:
            print("HTTP request:")
            print(scapy_packet.show())
        elif scapy_packet[inet.TCP].sport == 80:
            print("HTTP response:")
            print(scapy_packet.show())

    packet.accept()


try:
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    print("\nExiting script.\n")
