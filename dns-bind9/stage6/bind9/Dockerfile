FROM ubuntu/bind9:latest

WORKDIR /app
RUN apt-get update && apt-get install -y iproute2 tcpdump dnsutils iputils-ping traceroute neovim iptables

COPY ./bind9/bind9.sh /app/bind9.sh
RUN chmod +x /app/bind9.sh


ENTRYPOINT ["/app/bind9.sh"]
