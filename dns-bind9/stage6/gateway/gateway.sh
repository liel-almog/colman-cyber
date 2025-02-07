#!/bin/sh

echo 1 > /proc/sys/net/ipv4/ip_forward

# All the packet from the 192.168.3.0/24 to 192.168.2.0/24



nft -f block_outside_dns.sh
nft list ruleset > /etc/nftables.conf

# python3 ./dns_poisoning_without_id.py

tail -f /dev/null