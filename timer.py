# Python code licensed under GPL v3 by
# Joe Molloy (molloyjoe[at]gmail.com)

# Switches on Energenie socket no. 1 at Dusk
# using Astral package to calculate
# time of dusk

import RPi.GPIO as GPIO
from astral import *
from datetime import datetime
import pytz
import time

#Customise your city
city = 'Dublin'

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output (22, False)
    GPIO.output (18, False)
    GPIO.output (11, False)
    GPIO.output (15, False)
    GPIO.output (16, False)
    GPIO.output (13, False)


def check_time():
    a = Astral()
    location = a[city]
    sun = location.sun(local=True, date=datetime.now())
    dusk = sun['dusk']
    print "Dusk today is at %s" % dusk
    now = datetime.now()
    now = now.replace(tzinfo=pytz.UTC)
    print "Now it is %s" % now
    td = (dusk - now).seconds
    if td < 0:
    	print 'Need to check light'
        check_lights()
    else:
        print 'Need to sleep for %d' % td
        time.sleep(td)
        check_lights()


def check_lights():
    print 'Checking if light is already on...'
    print GPIO.input(11)
    print GPIO.input(15)
    print GPIO.input(16)
    print GPIO.input(13)
    if((GPIO.input(11) == 0 and GPIO.input(15) == 0 and GPIO.input(16) == 0 and GPIO.input(13) == 0) or (GPIO.input(11) == 1) and GPIO.input(15) == 1 and GPIO.input(16) == 1 and GPIO.input(13) == 0):
        print 'Light is off'
        turn_on_light()
    else:
        print 'Light already is on'


def turn_on_light():
    print 'Switching light on'
    GPIO.output(11,True)
    GPIO.output(15,True)
    GPIO.output(16,True)
    GPIO.output(13,True)
    time.sleep(0.1)
    GPIO.output (22, True)
    time.sleep(0.25)
    GPIO.output (22, False)       

setup_gpio()
check_time()
