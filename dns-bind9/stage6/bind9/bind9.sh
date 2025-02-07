#!/bin/sh

ip route del default
ip route add default via 192.168.3.20

docker-entrypoint.sh