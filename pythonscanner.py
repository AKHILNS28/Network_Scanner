import sys
import socket
import pingsweep, tcpscanner, service

def banner():
    print("=" * 50)
    print("     Python Network Scanner")
    print("     Ping • TCP Scan • Local Inspection")
    print("=" * 50)

def menu():
    print("\nChoose an option:")
    print("  1) Ping Sweep")
    print("  2) TCP Connect Scan")
    print("  3) Local Socket Inspection")
    print("  0) Exit")

def main():
    while True:
        banner()
        menu()

        try:
            choice = int(input("\nEnter your choice: ").strip())
        except ValueError:
            print("\n[!] Invalid input. Please enter a number.")
            continue

        match choice:
            case 1:
                addr = input("\nEnter the network address (e.g. 192.168.1.0/24): ")
                print("\n[+] Starting Ping Sweep...\n")
                pingsweep.pingsweep(addr)

            case 2:
                hostname = input("\nEnter hostname or IP address: ")
                try:
                    target_ip = socket.gethostbyname(hostname)
                    print(f"\n[+] Target resolved to {target_ip}")
                    print("[+] Starting TCP Connect Scan...\n")
                    tcpscanner.scanner(target_ip)
                except socket.gaierror:
                    print("\n[!] Invalid hostname or IP address")

            case 3:
                print("\n[+] Local Socket Inspection\n")
                service.service()

            case 0:
                print("\nExiting scanner. Goodbye")
                sys.exit()

            case _:
                print("\n[!] Invalid choice. Try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()