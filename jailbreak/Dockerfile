FROM python:3.10-slim

WORKDIR /server

ADD . .

RUN chmod 777 ./jailserver.py &&\
    chmod 777 ./jail.sh 

RUN groupadd -g 7007 7007 &&\
    useradd -u 7007 -g 7007 haha

USER haha

EXPOSE 7007

CMD [ "python3", "./jailserver.py" ]
