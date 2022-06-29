import urx
import time

v = 0.3
a = 0.3

def robot_connect(ip):
    return urx.Robot(ip, use_rt=True, urFirm=5.1)

def robot_set_speed(rob, speed):
    speedms = speed / 100
    global v
    v = speedms
    time.sleep(0.1)
    return

def robot_set_acceleration(rob, acc):
    accms2 = acc / 100
    global a
    a = accms2
    time.sleep(0.1)
    return
 
def robot_move_simple(rob, x, y, z):
    position = x, y, z, 0, 3.14, 0
    rob.movex("movej", position, acc=a, vel=v, wait=True, relative=False, threshold=None)

def robot_move_simple_rotated(rob, x, y, z):
    position = x, y, z, 2.2, 2.2, 0
    rob.movex("movej", position, acc=a, vel=v, wait=True, relative=False, threshold=None)
    
def robot_move(rob, x, y, z, rx, ry, rz):
    position = x, y, z, rx, ry, rz
    rob.movex("movej", position, acc=a, vel=v, wait=True, relative=False, threshold=None)

def robot_move_x(rob, mm):
    position = mm, 0, 0, 0, 0, 0
    rob.movex("movej", position, acc=a, vel=v, wait=True, relative=True, threshold=None)
    
def robot_move_y(rob, mm):
    position = 0, mm, 0, 0, 0, 0
    rob.movex("movej", position, acc=a, vel=v, wait=True, relative=True, threshold=None)
    
def robot_move_z(rob, mm):
    position = 0, 0, mm, 0, 0, 0
    rob.movex("movej", position, acc=a, vel=v, wait=True, relative=True, threshold=None)
      
def robot_move_joints_relative(rob, joint1, joint2, joint3, joint4, joint5, joint6):
    joints = joint1, joint2, joint3, joint4, joint5, joint6
    rob.movej(joints, acc=a, vel=v, wait=True, relative=True, threshold=None)

def robot_move_joint_position(rob, joint1, joint2, joint3, joint4, joint5, joint6):
    joints = joint1, joint2, joint3, joint4, joint5, joint6
    rob.movej(joints, acc=a, vel=v, wait=True, relative=False, threshold=None)

def robot_rotate_tool(rob, joint6):
    joints = 0.0, 0.0, 0.0, 0.0, 0.0, joint6
    rob.movej(joints, acc=a, vel=v, wait=True, relative=True, threshold=None)
   
def robot_move_list(rob, list):
    rob.movexs("movej", list, acc=a, vel=v, radius=0.01, wait=True, threshold=None)
    
def robot_set_tcp(rob, tcp):
    rob.set_tcp(tcp)
    time.sleep(0.1)
    return
    
def robot_send_program(rob, program):
    rob.send_program(program)
    time.sleep(0.1)
    return
    
def robot_wait(self):
    while not self.is_program_running():
        time.sleep(0.1)       
    return