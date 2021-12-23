# Origin image
FROM ubuntu:20.04

# Meta Information
LABEL Maintainer="Gal Birkman <galbirkman@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive

# Setup Server Environment
RUN apt update \
    && ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime && \
		apt install -y tzdata && \
		dpkg-reconfigure --frontend noninteractive tzdata && \
		apt install -y apache2 php libapache2-mod-php openssh-server && \
		rm -rf /var/www/html && \
		mkdir -p /run/sshd

# Setup Vulnerability Environment

ADD source.tar /var/www/

COPY ./init.sh /root

RUN chmod +x /root/init.sh

CMD ["/bin/bash", "-c" ,"/root/init.sh"]
