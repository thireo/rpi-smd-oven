#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
from datetime import datetime
import RPi.GPIO as GPIO


# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0


# Uncomment one of the blocks of code below to configure your Pi or BBB to use
# software or hardware SPI.

# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 24
DO  = 18
sensor = MAX31855.MAX31855(CLK, CS, DO)

# Raspberry Pi hardware SPI configuration.
#SPI_PORT   = 0
#SPI_DEVICE = 0
#sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# BeagleBone Black software SPI configuration.
#CLK = 'P9_12'
#CS  = 'P9_15'
#DO  = 'P9_23'
#sensor = MAX31855.MAX31855(CLK, CS, DO)

# BeagleBone Black hardware SPI configuration.
#SPI_PORT   = 1
#SPI_DEVICE = 0
#sensor = MAX31855.MAX31855(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# Loop printing measurements every second.
print('Press Ctrl-C to quit.')
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(2,GPIO.OUT)
#GPIO.output(2,GPIO.LOW)
pwm = GPIO.PWM(2,1)

dutycycle = 0

pwm.start(dutycycle)
state = 0
lasttime = datetime.now().timestamp()
while True:
    temp = sensor.readTempC()
    internal = sensor.readInternalC()
    if(state == 0): #PREHEAT
        if(temp > 120):
            dutycycle = 50
        else:
            dutycycle = 100
            #GPIO.output(2,GPIO.HIGH)
        if(temp > 130):
            print(datetime.now().timestamp(),'state=1')
            lasttime = datetime.now().timestamp()
            state = 1
            dutycycle = 0
            #GPIO.output(2,GPIO.LOW)
            continue
    elif(state == 1): #SOAKING
        if(lasttime+120 < datetime.now().timestamp()):
            print(datetime.now().timestamp(),'state=2')
            state = 2
            continue
        if(temp < 150):
            dutycycle = 50
            #GPIO.output(2,GPIO.HIGH)
        else:
            dutycycle = 0
            #GPIO.output(2,GPIO.LOW)
    elif(state == 2): #REFLOW HEATING
        if(temp > 200):
            dutycycle = 50
            #GPIO.output(2,GPIO.LOW)
        elif(temp > 210):
            dutycycle = 25
        else:
            dutycycle = 100
            #GPIO.output(2,GPIO.HIGH)
        if(temp > 220):
            print(datetime.now().timestamp(),'state=3')
            lasttime = datetime.now().timestamp()
            state = 3
            dutycycle = 0
            continue
    elif(state == 3): #REFLOW CYCLE
        if(lasttime+10 < datetime.now().timestamp()):
            print(datetime.now().timestamp(),'state=4')
            state = 4
            continue
        if(temp < 220):
            dutycycle = 25
            #GPIO.output(2,GPIO.HIGH)
        else:
            dutycycle = 0
            #GPIO.output(2,GPIO.LOW)
    else: #FINISHED
        dutycycle = 0
        #print('Dutycycle: 0%')
        print('COOLING PHASE')
        #pwm.ChangeDutyCycle(0)
        #GPIO.output(2,GPIO.LOW)
    with open((str(datetime.now().date())+'3.log'),'a') as f:
        teststring = str(datetime.now().time())+'\t%3f*C\t%3f*C\t%3d'%(temp,internal,dutycycle)
        print('State:\t',state,' : ',teststring)
        teststring += '\n'
        f.write(teststring)
    pwm.ChangeDutyCycle(dutycycle)
    #print('Dutycycle:\t%3d'%dutycycle)
    time.sleep(0.25)
