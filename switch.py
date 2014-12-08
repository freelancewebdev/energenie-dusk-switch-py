# Python code licensed under GPL v3 by
# Joe Molloy (molloyjoe[at]gmail.com)

# toggles energenie socket 1 when 
# connected to a Raspberry Pi with
# the energenie addon board

import RPi.GPIO as GPIO
from astral import *
from datetime import datetime
import pytz
import time
import sys

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    # GPIO.setwarnings(False)
    # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    # Select the signal used to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)
    # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)
    # Disable the modulator by setting CE pin lo
    GPIO.output (22, False)
    # Set the modulator to ASK for On Off Keying
    # by setting MODSEL pin lo
    GPIO.output (18, False)
    # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output (11, False)
    GPIO.output (15, False)
    GPIO.output (16, False)
    GPIO.output (13, False)

def toggle():
    if sys.argv[1] == '1':
        turn_on_light()
    else:
        turn_off_light()
    #GPIO.cleanup()

def turn_on_light():
    print 'Switching light on'
    GPIO.output(11,True)
    GPIO.output(15,True)
    GPIO.output(16,True)
    GPIO.output(13,True)
    # let it settle, encoder requires this
    time.sleep(0.1)
    # Enable the modulator
    GPIO.output (22, True)
    # keep enabled for a period
    time.sleep(0.25)
    # Disable the modulator
    GPIO.output (22, False)

def turn_off_light():
    print 'Switching light off'
    GPIO.output(11,True)
    GPIO.output(15,True)
    GPIO.output(16,True)
    GPIO.output(13,False)
    # let it settle, encoder requires this
    time.sleep(0.1)
    # Enable the modulator
    GPIO.output (22, True)
    # keep enabled for a period
    time.sleep(0.25)
    # Disable the modulator
    GPIO.output (22, False)

setup_gpio()
toggle()
