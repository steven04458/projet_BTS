#!/usr/bin/env python
import time
import serial
import traitement_data

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=5
)

while 1:
    x=ser.readline()
    x=x.decode("utf-8")
    traitement_data.treat(x)