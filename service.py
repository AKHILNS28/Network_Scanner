import psutil
import socket
import os

KERNEL_PREFIXES = (
    "kworker",
    "cpuhp",
    "migration",
    "rcu",
    "watchdog",
)

SYSTEM_LABEL = "System / kernel-managed"

def is_user_service(pid: int) -> bool:
    try:
        proc = psutil.Process(pid)

        if proc.name().startswith(KERNEL_PREFIXES):
            return False
        exe = proc.exe()
        if not exe or not os.path.exists(exe):
            return False
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def services_on_port(port: int):
    seen = set()
    results = []
    for conn in psutil.net_connections(kind="inet"):
        if not conn.laddr or conn.laddr.port != port:
            continue
        proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
        key = (proto, port)
        if key in seen:
            continue
        seen.add(key)
        if conn.pid is None:
            results.append((proto, SYSTEM_LABEL, None))
            continue
        if is_user_service(conn.pid):
            proc = psutil.Process(conn.pid)
            results.append((proto, proc.name(), conn.pid))
        else:
            results.append((proto, SYSTEM_LABEL, None))
    return results

def service():
    try:
        port = int(input("Enter port number: ").strip())
    except ValueError:
        print("[!] Invalid port number")
        return
    print(f"\n[+] Inspecting local services on port {port}")
    print("-" * 40)
    services = services_on_port(port)
    if not services:
        print("No service listening on this port")
        return
    for proto, name, pid in services:
        pid_str = f"(PID {pid})" if pid else ""
        print(f"{proto:<3} → {name} {pid_str}")