# Ollie Langhorst
# Robotics Research under Dr. Krauss
# 11/24/2015
# This script will generate a square wave. Connect a oscilliscope to 
# the GPIO pin and ground to measure.
# Modified code from author of pigpio
# See abyz.co.uk/rpi/pigpio for details on pigpio library
#
# You must start the pigpio deamon first with: sudo pigpiod 


import pigpio as p
import time

square = []

#Set output pin
GPIO = 4


square.append(p.pulse(1<<GPIO, 0, 0.5))
square.append(p.pulse(0, 1<<GPIO, 0.5))

pi = p.pi()
pi.set_mode(GPIO, p.OUTPUT)
pi.wave_add_generic(square)

wid = pi.wave_create()

if wid >= 0:
	pi.wave_send_repeat(wid)
	time.sleep(1)
	pi.wave_tx_stop()
	pi.wave_delete(wid)
	
pi.stop()
