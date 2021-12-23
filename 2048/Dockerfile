# Origin image
FROM ubuntu:16.04

# Meta Information
LABEL Maintainer="Gal Birkman <galbirkman@gmail.com>""

# Setup Server Environment
RUN apt update \
    && apt install -y apache2 php libapache2-mod-php

# Setup Vulnerability Environment
RUN rm -rf /var/www/html

ADD source.tar /var/www/

# Entry point
ENTRYPOINT service apache2 start && /bin/bash