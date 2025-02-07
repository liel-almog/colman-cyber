FROM python:3.12-bullseye

WORKDIR /app
COPY ./gateway/python/dns_poisoning.py .
COPY ./gateway/python/requirements.txt .

RUN apt update && \
    apt install -y iproute2 iptables tcpdump dnsutils neovim nftables iputils-ping && \
    apt clean && \
    pip install -r requirements.txt

# Copy the custom shell script into the container
COPY ./gateway/gateway.sh /app/gateway.sh

# Copy the nftables configuration file into the container
COPY ./gateway/block_outside_dns.sh block_outside_dns.sh

# Make the script executable
RUN chmod +x /app/gateway.sh

ENTRYPOINT ["sh", "-c", "/app/gateway.sh"]

