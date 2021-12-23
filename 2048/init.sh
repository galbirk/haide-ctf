#! /bin/bash


sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Change Apache Port
sed -i 's/\<VirtualHost \*\:80\>/\<VirtualHost \*\:80'"$APACHE_PORT"'\>/g' /etc/apache2/sites-enabled/000-default.conf


echo "root:Aa123456" | chpasswd

service apache2 start

exec 2>&1 /usr/sbin/sshd -D -e -p 2${SSH_PORT}
