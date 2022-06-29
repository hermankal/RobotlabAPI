import urx
import time

def conveyor_start(rob):
    rob.set_digital_out(5, 1)
    time.sleep(0.5)
    rob.set_digital_out(5, 0)
    
def conveyor_stop(rob):
    rob.set_digital_out(7, 1)
    time.sleep(0.1)
    rob.set_digital_out(7, 0)
    
def conveyor_speed(rob, speed):
    rob.send_program("set_analog_outputdomain(1, 1)")
    rob.set_analog_out(1, speed)
    
#Will add def for reversing direction later
#def conveyor_reverse(rob):
#   rob.set_digital_out(?, 1)
#   time.sleep(0.1)
#   rob.set_digital_out(?, 0)