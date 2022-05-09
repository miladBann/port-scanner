import socket
import termcolor


def scan(target, ports_to_scan):
    print(f"\n scanning for ip addrs {target}")
    for port in range(1, ports_to_scan):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect(ipaddress, port)
        print(termcolor.colored((f"[+] port open {port}"), "green"))
        sock.close()
    except:
        print(termcolor.colored((f"[-] port closed {port}"), "red"))


target = input(
    "inset the ip address witch you want to scan (spread by a space):  ")
ports_to_scan = int(input("Enter how many ports you want to scan:  "))

if " " in target:
    targets = target.split(" ")
    for new_target in targets:
        scan(new_target, ports_to_scan)
else:
    scan(target, ports_to_scan)
