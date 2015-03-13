# Sensu Experiment

This is me doing a crazy sensu experiment to understand it better. To
play along, you will need the following:

* [Boot2Docker](http://boot2docker.io/)
* [Docker Compose](https://docs.docker.com/compose/)
* Virtualenv or virtualenvwrapper
* A decent internet speed (the initial pull of docker containers can be
  EXPENSIVE)


## Getting Started

Once you have the above installed you're ready to start hacking.

* clone this repo

* `docker-compose up -d` - bring up all the pieces: rabbitmq, redis,
  sensu+uchiwa, rabbitmqagent

* navigate to http://192.168.59.103:3000/ to access the uchiwa
  dashboard. The login is admin/secret

* navigate to http://192.168.59.103:15672/ to access the rabbitmq
  management console. The login is guest/guest.

That's it! That's the main pieces we'll be interested in.

## Strucure

Configs used within containers:

- `etc/sensu` - configuration for sensu-server and uchiwa
- `etc/rabbit` - configuration for rabbitmq
- `etc/rabbit-agent` - configuration for the rabbitmq agent

For container building:

- `rabbit-agent` - builds the rabbit agent container
- `sensu` - used to build the sensu-server container

## Adding a New Check

Basically, just drop the plugin under `etc/rabbit-agent/plugins` and a
check file underneath `etc/sensu/conf.d`

## Set off an alarm

Install the `requirements.txt` dependencies and run `app.py` to dump
30,000 messages into a queue to trigger a warning. Do it again to
trigger a critical alert. 
