#!/bin/sh

# Remove the default route
ip route del default

# Add a new route to 192.168.1.30 via 192.168.1.20
ip route add default via 192.168.1.20

# Test DNS resolution by querying www.example.com
dig @192.168.2.30 www.example.com

# Keep the script running indefinitely (equivalent to 'tail -f /dev/null')
tail -f /dev/null
