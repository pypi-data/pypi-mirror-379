import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
import ipaddress

def scan_port(host, port, timeout=1):
    """
    Scans a single port on a given host.
    Returns a message indicating if the port is open or closed.
    """
    try:
        # Create a new socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout so the program doesn't hang
        s.settimeout(timeout)
        # Attempt to connect to the host and port
        s.connect((host, port))
        # If connect succeeds, the port is open
        return f"[+] Port {port} is OPEN"
    except (PermissionError):
        return f"[!] Port {port} requires elevated permissions to scan."
    
    except (socket.timeout, ConnectionRefusedError):
        # If a timeout or connection refused error occurs, the port is closed
        return f"[+] Port {port} is CLOSED"
    finally:
        # Always close the socket to free up resources
        s.close()

def is_local_or_private(target):
    # Checks if a target is 'localhost' or a private IP address.
    if target.lower() == 'localhost':
        return True
    try:
        # Check if the IP is in a private network range
        ip_obj = ipaddress.ip_address(target)
        return ip_obj.is_private
    except ValueError:
         # If it's not a valid IP address, it might be a domain name
        return False
        
def get_ports_to_scan(start, end):
    # Generates a list of ports to scan within a given range.
    return range(start, end+1)
        
def main():
    # The main function to run the port scanner.
    parser = argparse.ArgumentParser(description="A simple multithreaded port scanner.")
    parser.add_argument("target", help="The host to scan (IP address or domain name)")
    parser.add_argument("-p", "--port", help="Port range to scan (e.g., 1-100)", default="1-100")
    args=parser.parse_args()
    
    # --- Ethical Check ---
    if not is_local_or_private(args.target):
        response = input(f"Warning! You are about to scan a public host: {args.target}. Do you have explicit permission to do this? (yes/no): ")
        if response.lower() not in ("yes" or "y"):
            print("Scan aborted. Remember to only scan systems you have permission for.")
            exit()
            
    # --- Parse the port range ---
    try:
        start_port, end_port = map(int, args.port.split('-'))
        if start_port > end_port or start_port < 1 or end_port > 65535:
            raise ValueError
    except ValueError:
        print("Invalid port range. Please use a format like '1-100' with valid port numbers.")
        return
    print(f"[*] Starting scan on {args.target} for ports {start_port} to {end_port}...")
     
     # --- Multi-threaded scanning ---
    ports_to_scan = get_ports_to_scan(start_port, end_port)
     # Using a ThreadPoolExecutor to manage our threads efficiently
    with ThreadPoolExecutor(max_workers=50) as executor:
     # The map function applies our scan_port function to each item in ports_to_scan
        # We use a lambda to pass the constant host argument
        results = executor.map(lambda port: scan_port(args.target, port), ports_to_scan)
         
    for result in results:
        # Print the results as they become available
        print(result)
        
if __name__ == "__main__":
    main()