#!/usr/bin/env python

import netfilterqueue
import scapy.layers.inet as inet


def process_packet(packet):
    scapy_packet = inet.IP(packet.get_payload())
    print(scapy_packet.show())
    packet.accept()


try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    print("\nExiting script.\n")

