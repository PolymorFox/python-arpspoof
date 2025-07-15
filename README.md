# python-arpspoof

A simple arp spoofer written in python using [Scapy](https://scapy.net/)

## Requirements

- Python
- Pip
- Scapy

To install dependecies do:
```
pip install -r requirements.txt
```

If you encounter any errors during installation, just run:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements
```

## Usage

Here's what arguments you need to run to python-arpspoof:

```
python main.py -t <target address> -s <spoofed address>
```
