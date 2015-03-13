FROM ubuntu:14.04

RUN apt-get install wget -yq
RUN wget -q http://repos.sensuapp.org/apt/pubkey.gpg -O- | sudo apt-key add -
RUN echo "deb     http://repos.sensuapp.org/apt sensu main" > /etc/apt/sources.list.d/sensu.list

RUN apt-get update
RUN apt-get install sensu -yq

RUN \
  apt-get update && \
  apt-get install -y ruby ruby-dev ruby-bundler && \
  rm -rf /var/lib/apt/lists/*


RUN gem install sensu-plugin --no-rdoc --no-ri
RUN gem install carrot-top --no-rdoc --no-ri

CMD /opt/sensu/bin/sensu-client -c /etc/sensu/config.json

