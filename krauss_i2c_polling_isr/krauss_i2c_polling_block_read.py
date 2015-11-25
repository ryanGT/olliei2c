#~ Ollie Langhorst
#~ Robotics Research under Dr. Krauss
#~ November 23 2015

import smbus
import time
import serial_utils

bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04

n = 100

t1 = time.time()
responses = []
ilist = range(1,10)
testbyte = 0
sendindex_list = []
allbytes = []

for i in ilist:
    #bus.write_byte(SLAVE_ADDRESS, i)
    testbyte = bus.read_byte(SLAVE_ADDRESS)
    poll_count = 0
    while (testbyte != 1):
        poll_count += 1
        testbyte = bus.read_byte(SLAVE_ADDRESS)
    mylist = bus.read_block_data(SLAVE_ADDRESS,3)
    nlsb = mylist[0]
    nmsb = mylist[1]
    cursend = mylist[2]
    ## nlsb = bus.read_byte(SLAVE_ADDRESS)
    ## nmsb = bus.read_byte(SLAVE_ADDRESS)
    ## cursend = bus.read_byte(SLAVE_ADDRESS)
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
