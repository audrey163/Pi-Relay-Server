#!/usr/bin/python3

import RPi.GPIO as GPIO

class Relay():
    def __init__(self):
        self.channels = {'1' : 26,'2' : 19, '3' : 13, '4' : 6, '5' : 12, '6' : 16, '7' : 20,'8' : 21}

        GPIO.setmode(GPIO.BCM)
        for ch in list(self.channels):
            GPIO.setup(self.channels[ch], GPIO.OUT)
            GPIO.output(self.channels[ch], GPIO.HIGH)

    def __del__(self):
        GPIO.cleanup()

    def low(self,ch):
        GPIO.output(self.channels[ch], GPIO.LOW)

    def high(self,ch):
        GPIO.output(self.channels[ch], GPIO.HIGH)
