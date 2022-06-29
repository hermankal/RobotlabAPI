import urx
import time
import urllib.request
from API.GripperAPI import *
from API.ProximitySensorAPI import *
from API.URRobotAPI import *
from API.ConveyorAPI import *

# IP Address of the robot
robot2IP = "10.1.1.5"

# Counter for number of objects placed
count = 0

# Connect to the robot
rob2 = robot_connect(robot2IP)

# Open gripper
robot_send_program(rob2, rq_open())
time.sleep(0.15)

# Set tool center point
robot_set_tcp(rob2, (0.0,0.0,0.1755,0.0,0.0,0.0))
time.sleep(0.15)

# Start the conveyor belt
conveyor_start(rob2)
time.sleep(0.15)

# Set speed of the conveyor belt
conveyor_speed(rob2, 0.2)
time.sleep(0.15)

# Move robot into start position
# The first point is a point that is reachable no matter where the robot left of from earlier tasks
robot_move_simple(rob2, -0.4, 0.0, 0.1)
# The second point is the where it will pick objects from the conveyor belt
robot_move_simple(rob2, 0.05, 0.38, -0.02)
# Delays after movement commands is not needed, the API will wait for the command to complete before returning. 
# Sending commands to the robot before another is completed would result in the previous commands being cancelled

while True:
    # Gets the distance measures from the proximity sensor
    sensorvalue = sensor_proximity(3) # Port 3, where port 1 is the sensor closest to the door and sensor 4 is the one furthest away from the door. 4 sensors in total.
    
    # Print for testing
    print(str(sensorvalue))
    
    # If the distance measured is less then 40cm, it means an object is detected on the conveyor belt
    if sensorvalue < 40:
        #time.sleep(14.1)
        
        # The time to wait from when the sensor detected a object until the gripper should grab it
        # This delay needs to be changed based on the speed of the conveyor. 
        # Multiple sensors can be used to calculate the speed of the conveyor belt based on the time an object is detected and the distance between the sensors.
        time.sleep(7.7)
        
        # Close the gripper
        robot_send_program(rob2, rq_close())
        
        # A short delay to make sure the gripper has time to close before the robot stats moving
        time.sleep(0.15)
        
        # Move robot up (positive z direction) by 4 cm
        robot_move_z(rob2, 0.04)
        
        # Move robot to a point that is guaranteed to be reachable
        # Doing this is needed to make sure the robot does not calculate a path that goes through the robot, or somewhere that may hit the surroundings.
        # Movements that would go through the robot will make the robot throw an error about the destination not being reachable.
        robot_move_simple(rob2, -0.4, 0.0, 0.1)
        
        # Simple solution to choose a position on the tale to place the object depending on the count of objects placed before.
        # Will result in the object placed in a line on the table. To instead stack the objects, change the z coordinate instead of the y coordinate
        ycor = -0.4 + (count / 10)
        count = count + 1
        
        # Move robot to a point above where the object will be placed
        # First moving to coordinates above where it will place the object is done to avoid dragging the object accross the table or hit any other objects on the way
        robot_move_simple(rob2, -0.2, ycor, 0.1)
        
        # Moves the robot down by 9.7 cm
        robot_move_z(rob2, -0,097)
        
        # Open the gripper to release the object
        robot_send_program(rob2, rq_open())
        time.sleep(0.15)
        
        # Move the robot up by 10cm, to avoid hitting the object when moving away
        robot_move_z(rob2, 0,1)
        
        # Move robot to a point that is guaranteed to be reachable
        robot_move_simple(rob2, -0.4, 0.0, 0.1)
        
        # Move back to the point where it will pick objects from the conveyor belt
        robot_move_simple(rob2, 0.05, 0.38, -0.02)
    time.sleep(0.1)
    
