FROM debian:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    iproute2 \
    iptables \
    tcpdump \
    dnsutils \
    neovim \
    iputils-ping

# Copy the custom shell script into the container
COPY ./client/client.sh /app/client.sh

# Make the script executable
RUN chmod +x /app/client.sh


CMD ["/app/client.sh"]
