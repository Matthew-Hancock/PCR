#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Vector3
from Phidget22.Phidget import *
from Phidget22.Devices.MotorPositionController import *
import numpy as np

class Robotic_Manipulator:
    def __init__(self, arm_length):
        self.arm_length = arm_length
    
    def find_joint_angles(self,x,y,z):
        r = (x**2 + y**2 + z**2)**0.5
        max_dist = 2*self.arm_length
        if r > max_dist:
            rospy.logwarn("Desired position is out of range of the robot arm")
        else:
            yaw = np.atan2(y,x)*180/np.pi
            l = (x**2 + y**2)**0.5

            phi = np.arctan(z/l)
            l_prime = (l**2 + z**2)**0.5
            a_1 = np.arccos((l_prime/2)/self.arm_length)

            shoulder = phi + a_1 * 180/np.pi
            elbow = 2*a_1 * 180/np.pi

            rospy.loginfo("yaw: {:.2f} degrees".format(yaw))
            rospy.loginfo("shoulder: {:.2f} degrees".format(shoulder))
            rospy.loginfo("elbow: {:.2f} degrees".format(elbow))
    
    def move_to_pos(self, )

def main():
    yaw = MotorPositionController()
    shoulder = MotorPositionController()
    elbow = MotorPositionController()
    
    yaw.setHubPort(2)
    yaw.setDeviceSerialNumber(683092)

    shoulder.setHubPort(3)
    shoulder.setDeviceSerialNumber(683092)

    elbow.setHubPort(4)
    elbow.setDeviceSerialNumber(683092)
    
    yaw.openWaitForAttachment(5000)
    shoulder.openWaitForAttachment(5000)
    elbow.openWaitForAttachment(5000)
    
    yaw.setTargetPosition(50000)
    yaw.setEngaged(True)

def move_to_posCB(msg):
    RM = Robotic_Manipulator(24)
    RM.find_joint_angles(msg.x, msg.y, msg.z)

if __name__ == '__main__':
    #main()
    rospy.init_node('RM_pos_controller')
    rospy.Subscriber("probe_pos", Vector3, move_to_posCB)
    rospy.spin()