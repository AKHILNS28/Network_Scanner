import socket

def scanner(ip):
    for i in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        try:
            sock.connect((ip, i))
            print(f"Port {i} is OPEN")
        except ConnectionRefusedError:
            pass
        except socket.timeout:
            print(f"Port {i} is FILTERED")
        except OSError:
            pass
        finally:
            sock.close()