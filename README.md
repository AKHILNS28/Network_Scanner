# 🛰️ Python Network Scanner

A modular **Python-based network scanner** that performs **host discovery**, **TCP port scanning**, and **local service enumeration** using OS-level introspection.

This project is built for learning and demonstrating **networking fundamentals**, **socket programming**, and **Linux process inspection**, inspired by tools like `nmap`, `ss`, and `netstat`.

---

## 🚀 Features

### 🔍 Ping Sweep (Host Discovery)
- ICMP-based host discovery
- Identifies live hosts in a subnet
- Measures round-trip time (RTT)

### 🔐 TCP Connect Scan
- Multithreaded TCP connect scan
- Scans ports 1–1024
- Detects:
  - **OPEN**
  - **CLOSED**
  - **FILTERED** ports

### 🧠 Local Socket Inspection
- Enumerates **local services bound to ports**
- Maps **port → protocol → process → PID**
- Filters kernel threads
- Deduplicates IPv4 / IPv6 and multiple bindings

---

---
## ⚙️ Requirements

- Python 3.8+
- Linux (Ubuntu / Kali recommended)

### Python dependencies
```bash
pip install ping3 psutil
