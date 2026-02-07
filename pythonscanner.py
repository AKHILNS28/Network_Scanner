import sys
import socket
import pingsweep,tcpscanner

print('.....Welcome to Python Network Scanner.....')
print("1.Ping Sweep")
print("2.TCP Connect Scan")

try:
    choice=int(input("Enter your choice:"))
except ValueError:
    print('Invalid Choice')
    sys.exit()

match choice:
    case 1:
        addr=input("Enter the network address:")
        pingsweep.pingsweep(addr)
    case 2:
        try:
            hostname=input("Enter hostname or ip address:")
            tcpscanner.scanner(socket.gethostbyname(hostname))
        except socket.gaierror:
            print('Invalid hostname')
    case _:
        print('Invlid choice')