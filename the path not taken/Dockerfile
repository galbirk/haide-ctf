FROM nginx:alpine

ADD vulnerable.conf /etc/nginx/conf.d/default.conf

COPY 404.html 404.png index.html velcomen.png /usr/share/nginx/html/

WORKDIR /var/www/app/static

COPY secret.html secret.png ./

COPY flag.txt ../

EXPOSE 80

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
