#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix

lat = []
long = []
def plotPosCB(msg):
    lat.append(msg.latitude)
    long.append(msg.longitude)

if __name__ == '__main__':
    rospy.init_node('graph_gps')
    rospy.Subscriber("/fix", NavSatFix, plotPosCB)
    rospy.spin()