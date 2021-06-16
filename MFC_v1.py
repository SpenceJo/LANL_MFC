#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:48:17 2021

Script to query and read in data from the mass flow rate controlers

@author: spencerjordan
"""

import serial
import datetime
import time
import sys
import glob

def get_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(3,256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.u*')          ###Hardcoded this to what I needed with the '.u'
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

baudrate = 19200
serial_port = get_ports()
serial_port = serial_port[0]
ser = serial.Serial(serial_port, baudrate)

if ser.isOpen():
   
    ser.flushInput()
    ser.flushOutput()

    #ser.write(str.encode('\n'))

    reading = ser.readline().decode('utf-8')  ##Always hangs up here
                                              ##Works if changed to 'read()'

    print(reading)
    log_dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    time.sleep(2.0)    #time between readings
    f = open('../Desktop/control_data.txt','a')
    f.write(log_dt + '\n') #+ ' ' + reading)
    f.close


else:
    print("cannot open serial port")























