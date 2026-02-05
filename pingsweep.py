from ping3 import ping
import ipaddress

def pingsweep(ip):
    hosts=ipaddress.ip_network(ip,strict=False)
    try:
        for h in hosts.hosts():
            response=ping(str(h),unit='ms',timeout=1)
            if response:
                print(f"The IP {h} is reachable in {response} ms")
    except PermissionError:
        print("ICMP needs root Permission")
        
