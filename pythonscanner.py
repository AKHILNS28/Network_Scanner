import sys
import socket
import pingsweep,tcpscanner

print('.....Welcome to Python Network Scanner.....')
print("1.Ping Sweep")
print("2.TCP Connect Scan")

choice=int(input("Enter your choice:"))

match choice:
    case 1:
        addr=input("Enter the network address:")
        pingsweep.pingsweep(addr)
    case 2:
        hostname=input("Enter hostname or ip address:")
        tcpscanner.scanner(socket.gethostbyname(hostname))