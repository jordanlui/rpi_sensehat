from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sleep_time = 0.6
while True:
        
    r = randint(0,255)
    sense.show_letter("W", (r,0,0))
    sleep(sleep_time)

    r = randint(0,255)
    sense.show_letter("O", (0,0,r))
    sleep(sleep_time)

    r = randint(0,255)
    sense.show_letter("W", (0,r,0))
    sleep(sleep_time)

    r = randint(0,255)
    sense.show_letter("!",(r,r,r))
    sleep(sleep_time)
    sense.clear()
