#!/usr/sbin/python3
# -*- coding: utf-8 -*-
import socket
import _thread
import json
import sys


class Node:
    def __init__(self, ip):
        self.ip = ip
        self.id = hash(f"{ip}+rafael")
        self.porta = 12345
        self.sucessor = None
        self.antecessor = None


def servidor_p2p(udp, node):
    print(f"=> Iniciando servidor P2P (ip={node.ip}, porta={node.porta})")
    orig = ("", node.porta)
    udp.bind(orig)
    while True:
        msg, cliente = udp.recvfrom(1024)


def interface(node):
    while True:
        pass


def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    node = Node(ip=sys.argv[1])
    _thread.start_new_thread(servidor_p2p, (udp, node))
    interface(node)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("Modo de utilização: python3 main.py <ENDEREÇO_IP>")
        sys.exit(0)
