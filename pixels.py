# Pixel control
from sense_hat import SenseHat
from random import randint


yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255,0,0)
purple = (255,0,255)


sense = SenseHat()


x = randint(0,255)
y = randint(0,255)
z = randint(0,255)

sense.set_pixel(0,2,(purple))
sense.set_pixel(7,4,(x,y,z))

##sense.clear()
