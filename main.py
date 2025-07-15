from spoofer import spoof
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t",type=str)
parser.add_argument("-s",type=str)
parser.add_argument("-n",type=int)
args = parser.parse_args()

target_address = args.t
spoofed_address = args.s
ping_limit = args.n

spoof(target_address,spoofed_address,ping_limit)
