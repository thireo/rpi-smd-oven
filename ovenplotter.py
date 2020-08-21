import matplotlib.pyplot as plt
import csv
from datetime import datetime
import time
import numpy
import argparse
import sys



def main(args):
    parser = argparse.ArgumentParser(description="Plots temperature readings from given '-f LOGFILE.log' file.")
    parser.add_argument("-f", "--filename", default= '', required=False)
    args = parser.parse_args(args)
    plot(args.filename)

def plot(filename):

    timestamps = []
    thermos = []
    dutycycles = []
    diffs = []
    states = []
    timestampFormat = '%H:%M:%S.%f'
    i = 0
    print('Loading: ',filename,'...')
    #with open('oven-testing.log','r') as file:
    with open(filename,'r') as file:
        reader = csv.reader(file,delimiter='\t')
        for timestamp,thermo,internal,dutycycle,state in reader:
            
            temp = thermo.split('*C')
            dutycycles.append(int(dutycycle))
            states.append(int(state)*25)
            #temp2 = temp[1].split('*C')
            thermos.append(float(temp[0]))
            #print(timestamp)
            if(i==0):
                t1 = datetime.strptime(timestamp,timestampFormat)
                startOfTime = t1.hour*60*60+t1.minute*60+t1.second+t1.microsecond/1e6
                print(startOfTime)
                timestamps.append(0)
                i = 1
            else:
                t1 = datetime.strptime(timestamp,timestampFormat)
                elapsedTime = t1.hour*60*60+t1.minute*60+t1.second+t1.microsecond/1e6-startOfTime
                timestamps.append(elapsedTime)

    dffs = []
    t = []
    tt = []
    ttt = []
    #thermos[0]=0
    #thermos[1]=0
    firstval = thermos[0]
    print('firstval:\t%d'%firstval)
    t.append(0)
    t.append(0)
    for i in range(len(thermos)):
        ttt.append(thermos[i])
        if(i > 1):
            thermos[i] = (thermos[i]- firstval)#/0.25
            dffs.append((thermos[i]-thermos[i-1])/(timestamps[i]-timestamps[i-1]))
    thermos[0]=0
    thermos[1]=0
    print(thermos[0:4])

    diffs = numpy.diff(thermos)


    tt.append(0)
    tt.append(0)
    for i in range(len(dffs)):
        if(i > 1):
            t.append((dffs[i]*0.1+0.9*t[i-1]))
            tt.append((t[i]*0.1+0.9*tt[i-1]))

    d = []
    for i in range(len(diffs)):
        if(i > 1):
            d.append((diffs[i]*0.001+0.999*diffs[i-1]))
            #print(d[i-1])
    convv = [0]*(len(tt)+15000)
    dcs = []
    dc = 3
    kp = 2#0.6#4.5#50
    kd = 1#2500#100#7500
    ki = 0.001#0.0005#0.0035#1
    di = 0
    ed = 0
    dis = []
    ed = 0
    eds = []
    ds = []
    dt = 1
    desire = 90-firstval

    for k in range(len(tt)):
        tt[k] = tt[k]*4

    bob = []
    for i in range(15000):
        if(i>5000):
            desire = 130-firstval
        if(i>7500):
            desire = 138-firstval
        if(i>10000):
            desire = 165-firstval
        ds.append(desire+firstval)
        di += (desire-convv[i])*dt*ki
        dis.append(di)
        if(i > 1):
            ed = (((convv[i-1]-desire)-(convv[i]-desire))/dt)*kd
            eds.append(ed)
        dc = (((desire-convv[i])*kp)+ed+di)/100
        if(dc > 3):
            dc = 3
        elif(dc < 0):
            dc = 0
        dcs.append(dc)

        for k in range(len(t)):
            convv[k+i] += t[k]*dc
        convv[i] = convv[i] + firstval
        #bob.append(convv[i]-thermos[i])

        

    plt.style.use('dark_background')
    plt.subplot(3,1,1)
    plt.title(filename)
    plt.plot(timestamps,thermos,'r')
    #plt.plot(eds)
    plt.ylabel('Temperatur [C]')
    plt.xlabel('Tid [s]')
    plt.grid()
    plt.xlim(0,len(dcs))
    #plt.show()
    plt.subplot(3,1,2)

    #plt.figure()
    #plt.plot(timestamps,dutycycles,'g')
    #plt.plot(timestamps,states,'b')
    #plt.gca().invert_yaxis()
    plt.plot(dcs,'r')
    #plt.plot(t)
    #plt.plot(bob)
    #plt.plot(eds,'b')
    plt.ylabel('Dutycycle [%]')
    plt.xlabel('Tid [s]')
    plt.xlim(0,len(dcs))
    plt.grid()

    plt.subplot(3,1,3)
    #plt.plot(timestamps[1:len(timestamps)],diffs)
    #plt.plot(diffs)
    plt.plot(ds,'g')
    plt.plot(convv,'r')
    #plt.plot(timestamps,thermos,'b')
    #plt.plot(ttt,'b')
    plt.xlim(0,len(dcs))
    plt.grid()
    plt.legend(['desired','calc.','meas.'])
    plt.show()

def chipquik():
    print('chipquik')
    y = []
    for i in range(400):
        if(i<90):
            y.append(int(i*1.39+25))
        elif(i<180):
            y.append(int((i-90)*0.28+150))
        elif(i<210):
            y.append(int((i-180)*1.4+175))
        elif(i<240):
            y.append(int((i-210)*1.07+217))
        elif(i<270):
            y.append(int(249-(i-240)*1.07))
    plt.plot(y)
    plt.show()
        





if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
