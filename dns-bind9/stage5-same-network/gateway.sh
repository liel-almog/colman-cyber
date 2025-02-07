#!/bin/sh

apt update
apt install -y iproute2 iptables tcpdump dnsutils neovim nftables
apt clean

pip install -r requirements.txt

# iptables -A INPUT -p icmp -j DROP && iptables -A OUTPUT -p icmp -j DROP && python3 dns_poisoning.py
nft -f block_icmp.nft
nft list ruleset > /etc/nftables.conf

python3 dns_poisoning.py