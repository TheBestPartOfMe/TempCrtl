#Automatische Lüftersteuerung
#Maximilian Weber
#23.09.2020

import RPi.GPIO as GPIO
import time

maxtemp = 5000 #Start temperatur, Bsp: 45000 -> 45.000 C
headerPin = 14  #Header für Lüfter / Pin for the Fan
delay = 30      #Delay in Sekunden /Delay in seconds
tempData = "/sys/class/thermal/thermal_zone0/temp" 

GPIO.setmode(GPIO.BCM)
GPIO.setup(headerPin, GPIO.OUT)

while True:
        fileread = open(tempData, "r")
        temp = fileread.read()
        fileread.close()

        if int(temp) < maxtemp:
                GPIO.output(headerPin, GPIO.HIGH)
        else:
                GPIO.output(headerPin, GPIO.LOW)

        time.sleep(delay)
