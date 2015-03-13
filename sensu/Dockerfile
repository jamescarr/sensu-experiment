FROM ubuntu:14.04

RUN apt-get install wget -yq
RUN wget -q http://repos.sensuapp.org/apt/pubkey.gpg -O- | sudo apt-key add -
RUN echo "deb     http://repos.sensuapp.org/apt sensu main" > /etc/apt/sources.list.d/sensu.list

RUN apt-get update
RUN apt-get install sensu supervisor uchiwa -yq

ADD files/supervisord.conf /etc/supervisord.conf

EXPOSE 3000 4567

CMD ["/usr/bin/supervisord"]

