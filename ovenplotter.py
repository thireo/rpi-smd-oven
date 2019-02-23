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
    diffs = []
    timestampFormat = '%H:%M:%S.%f'
    i = 0
    print('Loading: ',filename,'...')
    #with open('oven-testing.log','r') as file:
    with open(filename,'r') as file:
        reader = csv.reader(file,delimiter='\t')
        for timestamp,thermo,internal in reader:
            #print(thermo)
            temp = thermo.split('*C')
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
                
    diffs = numpy.diff(thermos)

    plt.subplot(2,1,1)
    plt.title(filename)
    plt.plot(timestamps,thermos)
    plt.ylabel('Temperatur [C]')
    plt.xlabel('Tid [s]')
    plt.grid()
    plt.subplot(2,1,2)

    plt.plot(diffs)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
