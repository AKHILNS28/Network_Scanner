import socket
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 0.5
MAX_THREADS = 50
PORT_RANGE = range(1, 1025)

def scan_port(ip: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[OPEN]     {ip:<15} : {port:<5}")
        elif result == socket.errno.ECONNREFUSED:
            pass
        else:
            print(f"[FILTERED] {ip:<15} : {port:<5}")
    except socket.timeout:
        print(f"[FILTERED] {ip:<15} : {port:<5}")
    except OSError:
        pass
    finally:
        sock.close()

def scanner(ip: str):
    print(f"\n[+] Starting TCP Connect Scan on {ip}")
    print("-" * 40)

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for port in PORT_RANGE:
            executor.submit(scan_port, ip, port)

    print("\n[+] Scan completed\n")