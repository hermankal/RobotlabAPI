import time
from API.ProximitySensorAPI import *

while True:
    #sensor_proximity(1) gets the current distance measured by the first proximity sensor, where sensor 1 is the one closest to the door, and sensor 4 is the one furthest away from the door
    print("Sensor 1: " + str(sensor_proximity(1)))
    time.sleep(1)
    print("Sensor 2: " + str(sensor_proximity(2)))
    time.sleep(1)
    print("Sensor 3: " + str(sensor_proximity(3)))
    time.sleep(1)
    print("Sensor 4: " + str(sensor_proximity(4)))
    time.sleep(1)
time.sleep(10)