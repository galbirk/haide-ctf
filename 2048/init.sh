#! /bin/bash

exec 2>&1 /usr/sbin/sshd -D -e -p 2${SSH_PORT}

service apache2 start
