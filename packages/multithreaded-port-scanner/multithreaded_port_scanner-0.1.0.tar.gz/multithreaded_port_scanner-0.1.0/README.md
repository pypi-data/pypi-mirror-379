# Multithreaded Port Scanner

A **simple, multi-threaded port scanner** built in Python for **educational purposes**.  
This tool is intended to help learn Python sockets, threading, and CLI design. **Do not use it on networks you do not own or have explicit permission to scan.**

## Features
- Scan a range of ports on localhost or private networks.
- Multi-threaded scanning for faster results.
- Ethical check to warn users before scanning public IPs.

## Installation

### 1) From PyPI (after publishing)
```bash
pip install multithreaded-port-scanner
```

### 2) Directly from GitHub
You can clone the repo and install locally:

```bash
# Clone the repository
git clone https://github.com/Mohd-Yasir/Multithreaded-Port-Scanner
cd multithreaded-port-scanner

# Install using pip
pip install .
```

After installation, the CLI command `scanner` will be available:

```bash
scanner --help
```

## Usage Example

Scan localhost ports 1-100:

```bash
scanner localhost -p 1-100
```

Warning prompt will appear if you try to scan a public IP:

```text
Warning! You are about to scan a public host: <IP>. Do you have explicit permission to do this? (yes/no):
```

## Legal & Ethical Notice

This tool is for **educational use only**.

- Only scan machines you own or have explicit permission to scan.
- The author is not responsible for misuse.
- Do not share this tool for illegal activities.

## License

MIT License. See [LICENSE](LICENSE) for details.