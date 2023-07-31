#!/usr/bin/python

import rospy
from std_msgs.msg import Int8
from Phidget22.Phidget import *
from Phidget22.Devices.BLDCMotor import *
from Phidget22.Devices.MotorPositionController import *
import time

def velocity_CB(msg=0.5):
	bldcMotor0 = BLDCMotor()

	bldcMotor0.setHubPort(0)
	bldcMotor0.setDeviceSerialNumber(683092)

	bldcMotor0.openWaitForAttachment(5000)

	#bldcMotor0.setTargetPosition(50000)
	pos = bldcMotor0.getPosition()
	rospy.loginfo("Motor position" + str(pos))
	#bldcMotor0.setEngaged(True)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	bldcMotor0.close()

if __name__=='__main__':
	rospy.init_node("motor_vel_subscriber")

	sub = rospy.Subscriber("/motor_vel", Int8, callback=velocity_CB)

	rospy.loginfo("motor_vel_subscriber node has been started")

	velocity_CB()

	rospy.spin()