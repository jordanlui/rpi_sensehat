# Environment sensing
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
while True:
    
    orientation = sense.get_orientation()
    pitch = round(orientation['pitch'],3)
    roll = round(orientation['roll'],3)
    yaw = round(orientation['yaw'],3)
    print("pitch={0}, roll={1}, yaw={2}".format(pitch,roll,yaw))
    sleep(0.3)

