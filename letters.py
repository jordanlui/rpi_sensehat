from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

r = randint(0,255)
sense.show_letter("W", (r,0,0))
sleep(1)

r = randint(0,255)
sense.show_letter("O", (0,0,r))
sleep(1)

r = randint(0,255)
sense.show_letter("W", (0,r,0))
sleep(1)

r = randint(0,255)
sense.show_letter("!",(r,r,r))
sleep(1)
sense.clear()
