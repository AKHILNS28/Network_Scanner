from ping3 import ping
import ipaddress

def pingsweep(ip):
    hosts=ipaddress.ip_network(ip,strict=False)
    try:
        for h in hosts.hosts():
            response=ping(str(h),unit='ms',timeout=1)
            if response:
                print(f"{h} is reachable ({response:.2f} ms)")
    except PermissionError:
        print("ICMP requires root privileges or CAP_NET_RAW")
        
