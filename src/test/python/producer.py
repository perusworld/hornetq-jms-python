'''
@author: Saravana Perumal Shanmugam
'''

from stompest.config import StompConfig
from stompest.sync import Stomp
from datetime import date
import time
import logging

CONFIG = StompConfig('tcp://localhost:61613')
QUEUE = 'jms.queue.prodcons'

if __name__ == '__main__':
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    client = Stomp(CONFIG)
    client.connect()
    for index in range(10):
    	client.send(QUEUE, 'A Message ' + str(index) + ' At ' + str(date.today()))
    	time.sleep(1)
    	
    client.disconnect()
    
