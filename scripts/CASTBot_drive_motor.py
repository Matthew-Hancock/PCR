#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
# import odrive

def drive_CB(msg):

    # set odrive velocity to msg.data[0]
    
    rospy.loginfo(msg.data)
    rospy.loginfo(msg.data[0])
    

def listener():
    rospy.init_node("drive_motor")
    rospy.Subscriber("drive_vel", Float32MultiArray, drive_CB)
    rospy.spin()

if __name__=='__main__':
    
    # Connect to and initialize motor
    listener()    