#~ Ollie Langhorst
#~ Robotics Research under Dr. Krauss
#~ November 23 2015

import smbus
import time
import serial_utils

bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04

n = 10

t1 = time.time()
responses = []
ilist = range(1,10)
testbyte = 0
sendindex_list = []

for i in ilist:
    #bus.write_byte(SLAVE_ADDRESS, i)
    testbyte = bus.read_byte(SLAVE_ADDRESS)
    while (testbyte == 0):
        testbyte = bus.read_byte(SLAVE_ADDRESS)
    nlsb = bus.read_byte(SLAVE_ADDRESS)
    nmsb = bus.read_byte(SLAVE_ADDRESS)
    cursend = bus.read_byte(SLAVE_ADDRESS)
    sendindex_list.append(cursend)
    n_int = serial_utils.TwoIntBytesToInt(nmsb, nlsb)
    n_echo = serial_utils.Clean_Twos(n_int)
    responses.append(n_echo)
    
t2 = time.time()

dt = t2-t1
print 'responses = ' + str(responses)
print 'dt = %0.4g' % dt	
N = len(ilist)
tpl = dt/N
print('time per loop = %0.4g' % tpl)
