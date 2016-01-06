from haigha.connection import Connection
from haigha.message import Message

connection = Connection(
  user='guest', password='guest',
  vhost='/', host='127.0.0.1',
  heartbeat=None, debug=True)

ch = connection.channel()
ch.exchange.declare('test_exchange', 'direct')
ch.queue.declare('test_queue', auto_delete=True)
ch.queue.bind('test_queue', 'test_exchange', 'test_key')

for i in xrange(30000):
    ch.basic.publish( Message('body', application_headers={'hello':'world'}),
      'test_exchange', 'test_key' )

connection.close()
