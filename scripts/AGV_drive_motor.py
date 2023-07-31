#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from Phidget22.Phidget import *
from Phidget22.Devices.BLDCMotor import *
from Phidget22.Devices.MotorPositionController import *

def drive_CB(msg):
    bldcMotor0.setTargetVelocity(msg.data[0])
    
    rospy.loginfo(msg.data)
    rospy.loginfo(msg.data[0])
    

def listener():
    rospy.init_node("drive_motor")
    rospy.Subscriber("drive_vel", Float32MultiArray, drive_CB)
    rospy.spin()

if __name__=='__main__':
    bldcMotor0 = BLDCMotor()
    bldcMotor0.setHubPort(0)
    bldcMotor0.setDeviceSerialNumber(683092)
    bldcMotor0.openWaitForAttachment(5000)
    listener()
    bldcMotor0.close()
    