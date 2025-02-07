# DNS Assignment

### Exercise 1
To create the `rndc.key` file we just need to run `rndc-confgen -a`

To create the `dump.db` file you need to do those steps:

1. Enter to the container shell using `docker exec -it dns-auth-srv /bin/bash` 
2. Run `chown root:root /var/cache/bind/dump.db` - this will change the permissions for the file so we can write to it (I'm not sure why we have to do this step
   but we do). This file is the file `bind` will show it's cache.
   We defined the file location in `named.conf.options`, `dump-file` property.

#### Part 4
Doing a MitM attack over DNS.
When the client sends a DNS query to the server it does it from a random port and the clients always connects to port 53.
It there isn't a server the listens on port 53 the OS sends an ICMP response that says _port unreachable_, which means it could not connect.
When we sniff the network and we see a DNS query we are sending a response but because the OS sends the ICMP message first, the client which waits for a response get the ICMP message that says it could not connect hence, the client closes the port and then when our reponse gets to the clients, the client says the port unreachable as well and then sends another ICMP message.

The solution is to block the ICMP protocol - incoming and outgoing.

```bash
sudo iptables -A INPUT -p icmp --icmp-type any -j DROP
sudo iptables -A OUTPUT -p icmp --icmp-type any -j DROP
```