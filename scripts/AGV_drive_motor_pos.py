#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from Phidget22.Phidget import *
from Phidget22.Devices.BLDCMotor import *
from Phidget22.Devices.MotorPositionController import *
import time

def drive_CB(msg):
    valueA = msg.data[0]
    valueB = msg.data[1]
    #t1 = time.time()
    positionA = motorPositionController0.getPosition()
    positionB = motorPositionController1.getPosition()
    motorPositionController0.setTargetPosition(valueA+positionA)
    motorPositionController1.setTargetPosition(valueB + positionB)
    rospy.loginfo("Position A: " + str(positionA))
    rospy.loginfo("Next postion A: " + str(valueA+positionA))
    
    
    #print(time.time()-t1)   

def listener():
    rospy.init_node("drive_motor")
    accel = motorPositionController0.getAcceleration()
    vel = motorPositionController0.getVelocityLimit()
    rospy.loginfo("Acceleration: " + str(accel) + "   Velocity: " + str(vel))
    rospy.loginfo("drive_motor node started")
    rospy.Subscriber("/drive_vel", Float32MultiArray, drive_CB)
    rospy.spin()

if __name__=='__main__':
    Rescale_factor = 0.00229414803528


    motorPositionController0 = MotorPositionController()
    motorPositionController1 = MotorPositionController()
    motorPositionController0.setHubPort(0)
    motorPositionController1.setHubPort(1)
    motorPositionController0.setDeviceSerialNumber(683092)
    motorPositionController1.setDeviceSerialNumber(683092)
    motorPositionController0.openWaitForAttachment(5000)
    motorPositionController1.openWaitForAttachment(5000)
    motorPositionController0.setRescaleFactor(Rescale_factor)
    motorPositionController1.setRescaleFactor(Rescale_factor)
    motorPositionController0.setKi(0)
    motorPositionController1.setKi(0)
    motorPositionController0.setEngaged(True)
    motorPositionController1.setEngaged(True)

    

    motorPositionController0.setAcceleration(1)
    motorPositionController0.setVelocityLimit(2.5)
    motorPositionController1.setAcceleration(1)
    motorPositionController1.setVelocityLimit(2.5)
    
    
    listener()

if rospy.is_shutdown():
    motorPositionController0.close()
    motorPositionController1.close()
    print("Closed")
    