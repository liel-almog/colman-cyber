table ip nat {
    chain POSTROUTING {
        type nat hook postrouting priority srcnat; policy accept;
        oifname "eth0" masquerade
    }
}


table inet filter {
    chain forward {
        type filter hook forward priority 0; policy accept;

        # Block DNS responses to the bind9 container
        udp sport 53 drop
        tcp sport 53 drop

        udp dport 53 drop
        tcp dport 53 drop

        # Block all ICMP messages
        ip protocol icmp drop
    }

    chain input {
        type filter hook input priority 0; policy accept;

        # Drop all incoming ICMP packets
        ip protocol icmp drop
    }

    chain output {
        type filter hook output priority 0; policy accept;

        # Drop all outgoing ICMP packets
        ip protocol icmp drop
    }
}


table ip filter {
    chain input {
        type filter hook input priority 0; policy accept;
        
        # Drop all ICMP packets
        ip protocol icmp drop
    }
}
