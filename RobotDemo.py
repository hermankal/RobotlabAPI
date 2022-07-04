import time
from API.GripperAPI import *
from API.URRobotAPI import *

robot2IP = "10.1.1.5"

#Connect to the robot
rob2 = robot_connect(robot2IP) # (robotIP)

#Set tool center point
robot_set_tcp(rob2, (0.0,0.0,0.1755,0.0,0.0,0.0)) # (robot, (x, y, z, rx, ry, rz))
time.sleep(0.15)

#Acitvate gripper
print("Activate gripper")
robot_send_program(rob2, rq_activate()) # (robot, program)
time.sleep(2)

#Open gripper
print("Open gripper")
robot_send_program(rob2, rq_open()) # (robot, program)
time.sleep(2)

#Set robot speed
print("Set robot speed")
robot_set_speed(rob2, 50) # (robot, speed)
time.sleep(0.15)

#Close gripper
print("Close gripper")
robot_send_program(rob2, rq_close()) # (robot, program)
time.sleep(2)

#Move to xyz coordinate
print("Move to xyz coordinate")
robot_move_simple(rob2, -0.4, 0.0, 0.1) # (robot, x, y, z)
time.sleep(2)

#Move to xyz coordinate, with tool rotated 90 degrees
print("Move to xyz coordinate, with tool rotated 90 degrees")
robot_move_simple_rotated(rob2, -0.4, 0.0, 0.1) # (robot, x, y, z)
time.sleep(2)

#Move to x y z rx ry rz
print("Move to x y z rx ry rz")
robot_move(rob2, -0.4, 0.0, 0.2, 0.0, 3.14, 0.0) # (robot, x, y, z, rx, ry, rz)
time.sleep(2)

#Move in negative z direction (down) from current position
print("Move in negative z direction (down) from current position")
robot_move_z(rob2, -0.1) # (robot, meters)
time.sleep(2)

#Move in z direction (up) from current position
print("Move in z direction (up) from current position")
robot_move_z(rob2, 0.1) # (robot, meters)
time.sleep(2)

#Rotate tool, 2pi is a full rotation
print("Rotate tool, 2pi is a full rotation")
robot_rotate_tool(rob2, 6.28) # (robot, radians)
time.sleep(2)

#Rotate back
print("Rotate back")
robot_rotate_tool(rob2, -6.28) # (robot, radians)
time.sleep(2)

#Close connection to robot
print("Closing connection to the robot")
robot_close_connection(rob2)