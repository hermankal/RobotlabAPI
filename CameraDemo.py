import time
from API.SICKCameraAPI import *

cameraIP = "10.1.1.7"

camOffsetX = 25
camOffsetY = -385

while True: #Runs forever break with CTRL+C
    #If the camera detects an object, this function will return the coordinates of the object in the robots coordinate system
    #camOffsetX and camOffsetY is the difference between the x and y zero point of the robots coordinate system and the x and y zero point of the camera
    objectCoords = cam_get_xy_and_convert(cameraIP, camOffsetX, camOffsetY)
    #objectCoords = "xyz"
    print(objectCoords)
    time.sleep(2)
    
#Moving the robot to this coordinate can be done with robot_move_simple(robot, x, y, z) after importing the URRobotAPI (from API.URRobotAPI import *)
#robot_move_simple(rob, objectCoords["x"], objectCoords["y"], 0.1)
#Where 0.1 (10cm) is the height above the robots z zero point.

