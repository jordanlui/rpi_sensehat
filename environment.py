# Environment sensing
from sense_hat import SenseHat
from random import randint

sense = SenseHat()

# Parameters
T_low = 18.3
T_high = 26.7

while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t,1)
    p = round(p,1)
    h = round(h,1)

    if t > T_low and t < T_high:
        bg = (0,100,0)
    else:
        bg = (100,0,0) 
            

    msg = "Temperature = {0} C, Pressure = {1} mbar, Humidity = {2}%".format(t,p,h)

    sense.show_message(msg,scroll_speed=0.05, back_colour=bg)
