#!/bin/sh

ip route del default
ip route add default via 192.168.2.20

exec named -g