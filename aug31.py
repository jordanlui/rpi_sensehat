# SenseHAT RPi Evaluation
# element14
# Jordan Lui 2017

# Libraries

from sense_hat import SenseHat
from datetime import datetime


print('Element14 Raspberry Pi Evaluation')
##print 'test python version'


# Operating parameters
yellow = (255, 255, 0)
blue = (0, 0, 255)

sense = SenseHat()

##sense.show_message('Jordan Lui at MENRVA')
sense.show_message('RPi with element14!!!')
##sense.show_message(str(datetime.now()),0.1,text_colour=yellow, back_colour=blue)


sense.clear()
