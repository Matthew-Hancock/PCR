#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray, Float32
# import odrive

def drive_CB(msg):

    # set left odrive torque to msg.data[0]
    # set right odrive torque to msg.data[0]

    pub.Publish(hall_encoder_velocity)
    
    rospy.loginfo(msg.data)
    rospy.loginfo(msg.data[0])
    

def listener():
    rospy.init_node("bravo_drive_motor")
    rospy.Subscriber("/torque", Float32MultiArray, drive_CB)
    rospy.spin()

if __name__=='__main__':
    
    # Connect to and initialize motor
    pub = rospy.Publisher("/bravo_wheel_speed", Float32, queue_size=10)
    wheel_speed = Float32()
    listener()    