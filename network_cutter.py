#!/usr/bin/env python

import netfilterqueue


def process_packet(packet):
    packet.drop()


try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    print("\nExiting script.\n")
