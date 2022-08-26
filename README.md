# Python ethical hacking scripts
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
## :information_source: &nbsp; Introduction
This is my collection of simple python scripts for penetration testing and ethical hacking I create during my ethical hacking learning journey.
## :notebook_with_decorative_cover: &nbsp;Short script descriptions:
&nbsp;&nbsp;:small_orange_diamond: [ARP spoofer](arp_spoofer.py): Continuously spoofs the ARP cache of a target and the respective gateway to position yourself as AiTM. </br>
&nbsp;&nbsp;:small_orange_diamond: [DNS spoofer](dns_spoofer.py): Can, in combination with the ARP Spoofer, redirect the target from a predefined URL to a different predefined URL of your choosing by spoofing the DNS responses. </br>
&nbsp;&nbsp;:small_orange_diamond: [Download interceptor](download_interceptor.py): Redirects the target's HTTP file download to another URL by spoofing the HTTP response. Also needs to be used in combination with the ARP spoofer. </br>
&nbsp;&nbsp;:small_orange_diamond: [MAC changer](mac_changer.py): Simple script to change the MAC address of your own machine. </br>
&nbsp;&nbsp;:small_orange_diamond: [Network cutter](network_cutter.py): Simple tool, if used in combination with the ARP spoofer, blocks the network access of your target. </br>
&nbsp;&nbsp;:small_orange_diamond: [Network scanner](network_scanner.py): Scans a target network or target IP address and provides back a list of the respective IP addresses and corresponding MAC addresses. </br>
&nbsp;&nbsp;:small_orange_diamond: [Packet sniffer](packet_sniffer.py): Continuously scans the HTTP traffic of your target for possible username/password related buzzwords. To be used in combination with the ARP spoofer script. </br>
## :bow: &nbsp;Thanks to:
- Zaid Sabih from Zsecurity.org for the great course on which the scripts are based on
