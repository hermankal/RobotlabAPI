# RobotlabAPI

# Install requirements:
	pip install git+https://github.com/SintefManufacturing/python-urx
	pip install requests
	pip install urllib3

# GripperAPI.py
## 	This API generates programs for specific Robotiq-gripper tasks, which can then be sent to the UR-robot the gripper is connected to.
		
##	How to use the API
		robot_send_program(robot, rq_close())

		robot_send_program is from the URRobotAPI. Used to send programs to the robot.
		robot is the object created for the robot the gripper is connected to. Used to know which 	robot to send the program to.
		rq_close() creates a program using this API, that closes the gripper when sent to the robot.

	## Reset the gripper
		### Description
			Resets the gripper. May be used to reset the gripper if there are any issues.
		### Command
			rq_reset()
		### Example usage
			robot_send_program(robot, rq_reset())

	## Activate the gripper
		### Description
			Activates the gripper.
			The gripper needs to be activated for it to be used, this can also be done through the 		robot’s interface.
			The gripper will show a blue light on the side if it’s activated.
		### Command
			rq_activate()
		### Example usage
			robot_send_program(robot, rq_activate()) 
	## Close the gripper
		### Description
			Closes the gripper.
		### Command
			rq_close()
		### Example usage
			robot_send_program(robot, rq_close())

	## Open the gripper
		### Description
			Opens the gripper.
		### Command
			rq_open()
		### Example usage
			robot_send_program(robot, rq_open())

	## Set the gripper in a specific position
		### Description
			Sets the gripper in a specific position. May be used if you do not want to fully open 		or fully close the gripper.
		### Command
			rq_move(number)
		### Example usage
			robot_send_program(robot, rq_move(100))
		### Parameters
			number - Integer from 0-255, where 0 is fully opened and 255 is fully closed.


	## Set how much force the gripper will use
		### Description
			Sets a limit for how much force the gripper should use to grab objects. 
			Too low force may cause the gripper to not hold the object tightly enough, setting 		the force too high may damage the object.
		### Command
			rq_set_force(number)
		### Example usage
			robot_send_program(robot, rq_set_force(100))
		### Parameters
			number - Integer from 0-255, where 0 is minimum force and 255 is maximum force.

	## Set the speed of the gripper
		### Description
			Sets the speed the gripper.
		### Command
			rq_set_speed(number)
		### Example usage
			robot_send_program(robot, rq_set_speed(100))
		### Parameters
			number - Integer from 0-255, where 0 is minimum speed and 255 is maximum 			speed.


