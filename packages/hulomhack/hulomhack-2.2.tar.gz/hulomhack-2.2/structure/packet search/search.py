from socket import *
import socket
import ipaddress
from ipaddress import *

def ip(host):
    a = input('введите адрес сайта\n')
    print(f'The {a} IP Address is {socket.gethostbyname(a)}')

def helom(ip):
    p = input('введите ip\n')
    # initialize an IPv4 Address
    ip = ipaddress.IPv4Address(p)

    # print True if the IP address is global
    print("Is global:", ip.is_global)

    # print Ture if the IP address is Link-local
    print("Is link-local:", ip.is_link_local)

    # initialize an IPv4 Network
    network = ipaddress.IPv4Network(p)

    # get the network mask
    print("Network mask:", network.netmask)

    # get the broadcast address
    print("Broadcast addressdr:", network.broadcast_address)

    # print the number of IP adesses under this network
    print("Number of hosts under", str(network), ":", network.num_addresses)

    # get the supernet of this network
    print("Supernet:", network.supernet(prefixlen_diff=1))

    # iterate over the subnets of this network
    print("Subnets:")
    for subnet in network.subnets(prefixlen_diff=2):
        print(subnet)

def helom_ip(host):
    print(f'The {host} IP Address is {socket.gethostbyname(host)}')
    p = socket.gethostbyname(host)
    # initialize an IPv4 Address
    ip = ipaddress.IPv4Address(p)

    # print True if the IP address is global
    print("Is global:", ip.is_global)

    # print Ture if the IP address is Link-local
    print("Is link-local:", ip.is_link_local)

    # initialize an IPv4 Network
    network = ipaddress.IPv4Network(p)

    # get the network mask
    print("Network mask:", network.netmask)

    # get the broadcast address
    print("Broadcast addressdr:", network.broadcast_address)

    # print the number of IP adesses under this network
    print("Number of hosts under", str(network), ":", network.num_addresses)

    # get the supernet of this network
    print("Supernet:", network.supernet(prefixlen_diff=1))

    # iterate over the subnets of this network
    print("Subnets:")
    for subnet in network.subnets(prefixlen_diff=2):
        print(subnet)