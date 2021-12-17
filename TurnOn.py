import RPi.GPIO as GPIO
#select ur GPIO pin for the fan below
headerPin= 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(headerPin, GPIO.OUT)
GPIO.output(headerPin, GPIO.HIGH)
