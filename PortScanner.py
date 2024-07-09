import socket
import threading

target = input("Enter the IP address to scan: ")
port_range = range(1, 1024)

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port {} is open".format(port))
    s.close()

print("Scanning {}...".format(target))
for port in port_range:
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
