from socket import *
import socket
import ipaddress
from ipaddress import *

def connect(host, port):
    l = input('введите ip\n')
    o = input('введите порт (основной 8080 enter чтобы использовать этот порт)\n')
    if not o:
        o = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(l, o)