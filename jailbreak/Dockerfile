FROM python:3.10-slim

WORKDIR /server

ADD . .

RUN chmod 777 ./jailserver.py &&\
    chmod 777 ./jail.sh \ 
    && groupadd -g 7007 7007 \
    && useradd -u 7007 -g 7007 haha

USER haha

CMD [ "python3", "./jailserver.py" ]
