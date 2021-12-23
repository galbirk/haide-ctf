# Origin image
FROM ubuntu:20.04

# Meta Information
LABEL Maintainer="Gal Birkman <galbirkman@gmail.com>"

# Setup Server Environment
RUN apt update \
    && apt install -y apache2 php libapache2-mod-php &&\
    openssh-server && \
    systemctl enable ssh


# Setup Vulnerability Environment
RUN rm -rf /var/www/html

ADD source.tar /var/www/

COPY ./init.sh /root

CMD ["/bin/bash", "-c" ,"/root/init.sh"]