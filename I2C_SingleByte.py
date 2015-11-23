#~ Ollie Langhorst
#~ Robotics Research under Dr. Krauss
#~ November 23 2015

import smbus
import time

bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04

n = 3

t1 = time.time()
bus.write_byte(SLAVE_ADDRESS, n)
n_echo = bus.read_byte(SLAVE_ADDRESS)
t2 = time.time()

dt = t2-t1
print 'n = ', n
print 'n_echo = ', n_echo
print 'dt = ', dt	
