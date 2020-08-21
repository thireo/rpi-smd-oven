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
import argparse

def main(args):
    parser = argparse.ArgumentParser(description="OVEN THINGY MA BOB")
    parser.add_argument("-f", "--filename", default= '', required=False)
    args = parser.parse_args(args)
    reflow(args.filename)

def reflow(filename):
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
    # Loop printing measurements every second.
    print('Press Ctrl-C to quit.')
    GPIO.setup(2,GPIO.OUT)
    pwm = GPIO.PWM(2,1)

    dutycycle = 0
    soakingStarted = 0

    pwm.start(dutycycle)
    state = 0
    lasttime = datetime.now().timestamp()
    while True:
        temp = sensor.readTempC()
        internal = sensor.readInternalC()
        dutycycle = 25
        with open((str(datetime.now().date())+'-%s.log'%filename),'a') as f:
            teststring = str(datetime.now().time())+'\t%3f*C\t%3f*C\t%3d\t%3d'%(temp,internal,dutycycle,state)
            #print('State:\t',state,' : ',teststring)
            print(teststring)
            teststring += '\n'
            f.write(teststring)
        pwm.ChangeDutyCycle(dutycycle)
        time.sleep(0.25)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
