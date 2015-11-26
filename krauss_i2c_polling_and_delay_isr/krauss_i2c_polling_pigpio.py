#~ Ollie Langhorst
#~ Robotics Research under Dr. Krauss
#~ November 23 2015
from matplotlib.pyplot import *

import smbus
import time
import serial_utils
from numpy import *

#bus = smbus.SMBus(1)
SLAVE_ADDRESS = 0x04

# the pigpio approach doesn't seem to work at all
import pigpio

pi = pigpio.pi()

handle = pi.i2c_open(1, SLAVE_ADDRESS)

n = 100

t1 = time.time()
responses = []
ilist = range(1,n)
testbyte = 0
sendindex_list = []
allbytes = []
ms = 1.0/1000
sleep_time = 0.1*ms
echo_responses = []

for i in ilist:
    #bus.write_byte(SLAVE_ADDRESS, i)
    #testbyte = bus.read_byte(SLAVE_ADDRESS)
    (length, testbyte) = pi.i2c_read_device(handle, 1)#<-- hangs here
    poll_count = 0
    while (testbyte != 1):
        poll_count += 1
        time.sleep(sleep_time)#asking for 1/10th of millisecond
        #testbyte = bus.read_byte(SLAVE_ADDRESS)
        (length, testbyte) = pi.i2c_read_device(handle, 1)
    imsb, ilsb = serial_utils.two_bytes(i)
    #bus.write_i2c_block_data(SLAVE_ADDRESS, 1, [imsb,ilsb])
    #data = bus.read_i2c_block_data(SLAVE_ADDRESS, 4)
    (length, data) = pi.i2c_read_device(handle, 4)
    nlsb = data[0]
    nmsb = data[1]
    vlsb = data[2]
    vmsb = data[3]
    #nlsb = bus.read_byte(SLAVE_ADDRESS)
    #nmsb = bus.read_byte(SLAVE_ADDRESS)
    #vlsb = bus.read_byte(SLAVE_ADDRESS)
    #vmsb = bus.read_byte(SLAVE_ADDRESS)
    #cursend = bus.read_byte(SLAVE_ADDRESS)
    currow = [testbyte, nlsb, nmsb, cursend, vlsb, vmsb, poll_count]
    allbytes.append(currow)
    sendindex_list.append(cursend)
    n_int = serial_utils.TwoIntBytesToInt(nmsb, nlsb)
    n_echo = serial_utils.Clean_Twos(n_int)
    echo_int = serial_utils.TwoIntBytesToInt(vmsb,vlsb)
    echo_ans = serial_utils.Clean_Twos(echo_int)
    responses.append(n_echo)
    echo_responses.append(echo_ans)
    
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

figure(1)
clf()
ilist
plot(ilist, echo_responses,'ro')

pi.i2c_close(handle)

pi.stop()

show()
