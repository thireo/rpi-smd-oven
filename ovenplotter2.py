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
            if(temp[0] != 'nan'):
                dutycycles.append(int(dutycycle))
                states.append(int(state)*25)
                #temp2 = temp[1].split('*C')
                thermos.append(float(temp[0]))
                #print(float(thermo[0]))
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
    t.append(0)
    t.append(0)
    print(len(thermos))
    for i in range(len(thermos)):
        ttt.append(thermos[i])
        if(i > 1):
            thermos[i] = (thermos[i])#- thermos[0])
            dffs.append((thermos[i]-thermos[i-1])/(timestamps[i]-timestamps[i-1]))
    thermos[0]=0
    thermos[1]=0
    print(thermos[0:4])

    diffs = numpy.diff(thermos)
    print(len(diffs))

    tt.append(0)
    tt.append(0)
    for i in range(len(dffs)):
        if(i > 1):
            t.append((dffs[i]*0.25+0.75*t[i-1]))
            tt.append((t[i]*0.1+0.9*tt[i-1]))

    #for i in range(len(tt)):
        #print('%d - %d'%(i,thermos[i]))
    #diffs = numpy.diff(thermos,4)


    plt.style.use('dark_background')
    plt.subplot(3,1,1)
    plt.title(filename)
    plt.plot(timestamps,thermos,'r')
    plt.ylabel('Temperatur [C]')
    plt.xlabel('Tid [s]')
    plt.grid()
    #plt.show()
    plt.xlim(0,200)
    plt.subplot(3,1,2)

    #plt.figure()
    plt.plot(timestamps,dutycycles,'g')
    plt.plot(timestamps,states,'b')
    #plt.gca().invert_yaxis()
    plt.ylabel('Dutycycle [%]')
    plt.xlabel('Tid [s]')
    plt.grid()
    plt.xlim(0,200)

    plt.subplot(3,1,3)
    #plt.plot(timestamps[1:len(timestamps)],diffs)
    plt.plot(timestamps[0:len(t)],t)
    plt.xlim(0,200)
    plt.ylim(-1.5,1.5)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
