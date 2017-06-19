#!/usr/bin/python2
"""
sp00ky skelet0n
"""
import socket
from base64 import *
from scapy.all import *
from struct import *

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def auth(packet):
    ip = get_ip_address()
    proto = "tcp"
    dport =80
    if packet.haslayer(IP) and packet.getlayer(IP).src == ip:
        if packet.haslayer(TCP) and packet.getlayer(TCP).dport == dport:
            if packet.haslayer(Raw) and "Authorization: Basic" in packet.getlayer(Raw).load:
                cred = packet.getlayer(Raw).load
                cred = cred[cred.find("Authorization: Basic ")+ len("Authorization: Basic "):cred.find("=")]
                missing_padding = len(cred) % 4
                if missing_padding != 0:
                    cred += b'='* (4 - missing_padding)
                cred = base64.b64decode(cred)
                return "WARNING: Unprotected credentials! %s" %cred



def main():
    sniff(prn=auth, store=0)

if __name__=="__main__":
    main()
