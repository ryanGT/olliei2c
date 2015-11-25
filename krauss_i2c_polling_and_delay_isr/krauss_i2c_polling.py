#~ Ollie Langhorst
#~ Robotics Research under Dr. Krauss
#~ November 23 2015

import smbus
import time
import serial_utils
from numpy import *

bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04

n = 100

t1 = time.time()
responses = []
ilist = range(1,n)
testbyte = 0
sendindex_list = []
allbytes = []
ms = 1.0/1000
sleep_time = 0.1*ms

for i in ilist:
    #bus.write_byte(SLAVE_ADDRESS, i)
    testbyte = bus.read_byte(SLAVE_ADDRESS)
    poll_count = 0
    while (testbyte != 1):
        poll_count += 1
        time.sleep(sleep_time)#asking for 1/10th of millisecond
        testbyte = bus.read_byte(SLAVE_ADDRESS)
    nlsb = bus.read_byte(SLAVE_ADDRESS)
    nmsb = bus.read_byte(SLAVE_ADDRESS)
    cursend = bus.read_byte(SLAVE_ADDRESS)
    currow = [testbyte, nlsb, nmsb, cursend, poll_count]
    allbytes.append(currow)
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

test_r = array(responses)-responses[1]+1
test_diff = test_r-arange(n-1)

print('='*30)
print('test_diff = ')
print(str(test_diff))