#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float32
from sensor_msgs.msg import Imu

def alpha_wheel_speed(msg):
    global aws # alpha wheel speed
    aws = msg

def bravo_wheel_speed(msg):
    global bws # bravo wheel speed
    bws = msg

def imu(msg):
    global imu_data
    imu = msg

def torque_CB(aws, bsw):
    desired_vel = 1
    # control torque to drive fleet velocity to desired value, msg
    tau_alpha = nan
    tau_bravo = nan
    torque.data = [tau_alpha, tau_bravo]
    pub.Publish(torque)

    rate.sleep()

if __name__ == '__main__':
    rospy.init_node("torque_controller")
    rospy.Subscriber("/imu",Imu, imu)
    rospy.Subscriber("/alpha_wheel_speed",Float32,alpha_wheel_speed)
    rospy.Subscriber("/bravo_wheel_speed",Float32,bravo_wheel_speed)
    pub = rospy.Publisher("/torque",Float32MultiArray, queue_size = 10)
    rate = rospy.Rate(10)

    torque = Float32MultiArray()