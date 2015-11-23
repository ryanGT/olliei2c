#~ Ollie Langhorst
#~ Robotics Research under Dr. Krauss
#~ November 23 2015

import smbus
import time

bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04

n = 3

t1 = time.time()
responses = []

for i in range(1,10):
    bus.write_byte(SLAVE_ADDRESS, i)
    n_echo = bus.read_byte(SLAVE_ADDRESS)
    responses.append(n_echo)
    
t2 = time.time()

dt = t2-t1
print 'responses = ' + str(responses)
print 'dt = %0.4g' % dt	
