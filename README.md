![ARPKiller](https://github.com/user-attachments/assets/3c879938-7287-4ab3-a103-520eaea56511)


# ARPKiller
ARPKiller is a tool developed in Python3 whose function is to disconnect one or more devices from the internet in a local network. To achieve this, it poisons the ARP traffic to make the victim's machine believe that your device is the gateway, thereby ensuring that the victim's network traffic never reaches the internet.

### How does it work?

ARPKiller uses the arpspoof utility from dsniff to route the victim's traffic through your machine instead of the gateway (like a man-in-the-middle attack, but without redirecting the traffic back to the gateway)

![image](https://github.com/user-attachments/assets/86935b70-357f-40d1-9583-305b3633f0e5)

To prevent the traffic from being automatically redirected to the gateway, a 0 is added to the file /proc/sys/net/ipv4/ip_forward to disable packet forwarding (in case it is enabled)

![image](https://github.com/user-attachments/assets/1350d0d3-d89a-4d55-a901-c4e6dabcf458)

### Installation

```shell
git clone https://github.com/boxvox1/arpkiller.git
cd arpkiller
chmod +x arpkiller.py
```

### Usage

```shell
python3 arpkiller.py
```

---



