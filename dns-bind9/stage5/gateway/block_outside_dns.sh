#!/usr/sbin/nft -f

table inet filter {
    chain forward {
        type filter hook forward priority 0; policy accept;
        ip protocol icmp drop
        ip6 nexthdr icmpv6 drop

        # Allow forwarded DNS traffic within the local network
        ip saddr 192.168.0.0/16 udp dport 53 ip daddr 192.168.0.0/16 accept
        ip saddr 192.168.0.0/16 tcp dport 53 ip daddr 192.168.0.0/16 accept
        # Block all other forwarded DNS traffic
        udp sport 53 drop
        tcp sport 53 drop
    }
}
