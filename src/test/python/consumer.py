'''
@author: Saravana Perumal Shanmugam
'''

from stompest.config import StompConfig
from stompest.protocol import StompSpec
from stompest.sync import Stomp
import logging

CONFIG = StompConfig('tcp://localhost:61613', version=StompSpec.VERSION_1_0)
QUEUE = 'jms.queue.prodcons'

if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    client = Stomp(CONFIG)
    client.connect()
    client.subscribe(QUEUE, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL})
    while True:
        frame = client.receiveFrame()
        print 'Got %s' % frame.body
        client.ack(frame)
        if frame.body == 'done':
        	break
    client.disconnect()
    
