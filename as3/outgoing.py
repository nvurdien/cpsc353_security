#!/usr/bin/python2
"""
this program keeps track of the destination IP addresses it sees when it
encounters a TCP packet whose source address is your computer's IP address
"""
import socket
from scapy.all import *

def get_ip_address():
    """
    gets local IP address
    :returns local IP
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

st = set()
this_ip = get_ip_address()

def resolve_host(ip):
    """
    finds if the IP address has a hostname
    :param ip: IP address
    :returns destination hostname or destination IP address if hostname does not exist
    """
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.error:
        return ip

def print_new_ip(pkt):
    """
    prints the destination hostname or destination IP address that connect with your IP
    :param pkt: a scapy packet file
    :returns destination hostname or destination IP address if hostname does not exist
    """
    if IP in pkt:
        src_ip = pkt[IP].src
        dest_ip= pkt[IP].dst
        if src_ip == this_ip and dest_ip not in st:
            st.add(dest_ip)
            return resolve_host(dest_ip)

def main():
    sniff(prn=print_new_ip,store=0)

if __name__=="__main__":
    main()
