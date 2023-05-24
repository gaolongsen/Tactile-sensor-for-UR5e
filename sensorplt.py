# Author: Longsen Gao
# Date: 05-22-2023

import serial
import time
import matplotlib.pyplot as plt
import numpy as np

serialport = serial.Serial()
serialport.port = '/dev/ttyUSB1' # Depends on your serial number on your Ubuntu system
serialport.baudrate = 9600
serialport.bytesize = 8
serialport.parity = serial.PARITY_NONE
serialport.stopbits = 1
serialport.timeout = 0.001
serialport.close()

plt.ion()   # Open a drawing window
ax = []     # Define an empty list of x-axis to receive dynamic data
ay = []
i = 0
while 1:
    if not serialport.is_open:
        serialport.open()
    time.sleep(0.05)  # Time setting reference serial port transmission rate
    num = serialport.inWaiting()
    n = 0
    if num > 0:
        data = serialport.read(num).decode('utf-8')
        tem = data.replace('\r', '')
        tem = tem.split('\n')
        length = range(len(tem))
        for n in length:
            if tem[n] == '':
                tem[n] = '0'

        test_list = list(map(int, tem))
        cor_force = np.max(test_list)
        print('Force:', cor_force)
        ax.append(i)  # Add i to the data of the x-axis
        ay.append(cor_force)
        plt.figure('Pressure Detection')
        plt.clf()  # Clear the previously drawn diagram
        plt.title('Pressure line chart')
        plt.ylabel('Pressure /N')
        plt.xlabel('Time /s')
        plt.axis([0, i + 0.05, 0, 1000])
        plt.plot(ax, ay)  # Draw a graph of the current ax list and the values in the ay list
        plt.pause(0.1)  # stop 1s
        plt.ioff()  # Close the drawing window
        i = i + 0.05
