#!/usr/bin/python2
"""
sp00ky skelet0n
"""
import socket
from scapy.all import *

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

s = set()
this_ip = get_ip_address()

def main():
    sniff(prn=print_new_ip,store=0)

def resolve_host(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.error:
        return ip

def print_new_ip(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        dest_ip= pkt[IP].dst
        if src_ip == this_ip and dest_ip not in s:
            s.add(dest_ip)
            return resolve_host(dest_ip)

if __name__=="__main__":
    main()
