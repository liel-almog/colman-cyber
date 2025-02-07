#!/bin/sh

nft -f block_outside_dns.sh
nft list ruleset > /etc/nftables.conf

python3 ./dns_poisoning.py