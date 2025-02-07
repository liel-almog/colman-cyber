# Stage 3
To create the `rndc.key` file we just need to run `rndc-confgen -a`

To create the `dump.db` file you need to do those steps:

1. Enter to the container shell using `docker exec -it dns-auth-srv /bin/bash` 
2. Run `chown root:root /var/cache/bind/dump.db` - this will change the permissions for the file so we can write to it (I'm not sure why we have to do this step
   but we do). This file is the file `bind` will show it's cache.
   We defined the file location in `named.conf.options`, `dump-file` property.