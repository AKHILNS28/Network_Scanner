import socket
from concurrent.futures import ThreadPoolExecutor

def scan(args):
    ip,port=args
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
        print(f"[+] {ip:<15} : {port:<5} OPEN")
    except ConnectionRefusedError:
        pass
    except socket.timeout:
        print(f"[+] {ip:<15} : {port:<5} FILTERED")
    except OSError:
        pass
    finally:
        sock.close()

def scanner(ip):
    with ThreadPoolExecutor(max_workers=50) as pool:
        tasks=[(ip,port) for port in range(1,1025)]
        pool.map(scan,tasks)