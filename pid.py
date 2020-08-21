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
    GPIO.setup(5,GPIO.OUT)
    GPIO.setup(6,GPIO.OUT)
    GPIO.setup(0,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)

    led2 = GPIO.PWM(0,2)
    led1 = GPIO.PWM(6,2)
    led0 = GPIO.PWM(5,2)
    buzz = GPIO.PWM(13,2048)



    pwm = GPIO.PWM(2,1)

    dutycycle = 0

    dc = 1
    kp = 2#0.6#4.5#50
    kd = 1#2500#100#7500
    ki = 0.001#0.0005#0.0035#1

    #kp = 1#0.6#4.5#50
    #kd = 5#50#100#7500
    #ki = 0.0005#0.0005#0.0035#1
    di = 0
    ed = 0
    desire = 90
    lasttemp = 0
    dt = 1

    notStarted = 1
    pwm.start(dutycycle)
    state = 0
    lasttime = datetime.now().timestamp()

    buzzno = 0

    while True:
        temp = sensor.readTempC()
        #temp = temp
        if(notStarted):
            lasttemp = temp
        internal = sensor.readInternalC()
        if(state == 0): #PREHEAT
            desire = 200
            if(temp > 130):
                print(datetime.now().timestamp(),'state=1')
                lasttime = datetime.now().timestamp()
                state = 1
                desire = 130
                led0.start(100)
                continue
        elif(state == 1): #SOAKING
            if(lasttime+(120*1.5) < datetime.now().timestamp()):
                desire = 138
                state = 2
                led1.start(100)
                continue
        elif(state == 2): #REFLOW
            kd = 2
            kp = 10
            if(temp > 138):
                state = 3
                desire = 170
                lasttime = datetime.now().timestamp()
                print(datetime.now().timestamp(),'state=3')
                led2.start(100)
                continue
        elif(state == 3):
            if(lasttime+40 < datetime.now().timestamp()):
                state = 4
                led0.start(50)
                led1.start(50)
                led2.start(50)
                continue
        elif(state == 4): #COOLING
            if(buzzno<4):
                if(buzzno%2==0):
                    buzz.start(50)
                else:
                    buzz.stop()
                buzzno+=1
            else:
                buzz.stop()
            desire = 0
            dc = 0
            print('COOLING PHASE!!!')
        else:
            print('STATE ERROR') 
        ed = (((lasttemp-desire)-(temp-desire))/dt)*kd
        di += (desire-temp)*dt*ki
        dc = (((desire-temp)*kp)+ed+di)

        print('%d-%d-%d'%(ed,di,((desire-temp)*kp)))
        lasttemp = temp
        if(dc > 100):
            dc = 100
        elif(dc < 0):
            dc = 0
        print(dc)

        with open((str(datetime.now().date())+'-%s.log'%filename),'a') as f:
            teststring = str(datetime.now().time())+'\t%3f*C\t%3f*C\t%3d\t%3d'%(temp,internal,dc,state)
            #print('State:\t',state,' : ',teststring)
            print(teststring)
            teststring += '\n'
            f.write(teststring)
        pwm.ChangeDutyCycle(dc)
        time.sleep(dt)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
