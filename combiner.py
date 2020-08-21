import os

for file in os.listdir('C:/Gits/Rpi SMD Oven/test'):
    if('.log' in file):
        with open(file,'r') as f:
            
