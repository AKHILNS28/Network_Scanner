from ping3 import ping
import ipaddress

TIMEOUT = 1
UNIT = "ms"

def pingsweep(network: str):
    try:
        net = ipaddress.ip_network(network, strict=False)
    except ValueError:
        print("[!] Invalid network address")
        return
    print(f"\n[+] Starting Ping Sweep on {net}")
    print("-" * 45)
    try:
        for host in net.hosts():
            response = ping(str(host), timeout=TIMEOUT, unit=UNIT)

            if response:
                print(
                    f"[ALIVE] {str(host):<15}  "
                    f"RTT: {response:>6.2f} ms"
                )
    except PermissionError:
        print("\n[!] ICMP requires root privileges or CAP_NET_RAW")
        print("    Try: sudo setcap cap_net_raw+ep $(which python3)")