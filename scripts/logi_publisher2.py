#!/usr/bin/python

import rospy
from std_msgs.msg import Float32MultiArray
import pygame

def controller_input():
    valueR = 0
    valueL = 0
    prev_valueR = 0  # variable to keep track of previous value
    prev_valueL = 0
    hold_switch = False
    interval = 1
    while not rospy.is_shutdown():
        for event in pygame.event.get():  # get pygame event
            #if event.type == pygame.JOYDEVICEREMOVED or (event.type == pygame.JOYBUTTONUP and event.button == 2):  # if user quits
                #done = True
            rospy.loginfo("Event: " + str(event))
            if event.type == pygame.JOYBUTTONUP and event.button == 4:
                hold_switch = False
                prev_valueR = 0
                prev_valueL = 0
                valueR = 0
                valueL = 0
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                hold_switch = True
            if event.type == pygame.JOYHATMOTION and event.hat == 0:
                interval += event.value[1] * 0.2
            if event.type == pygame.JOYAXISMOTION and hold_switch:
                if event.axis == 3:
                    valueR = round(event.value, 1)*interval
                    prev_valueR = valueR
                elif event.axis == 1:
                    valueL = -round(event.value, 1)*interval
                    prev_valueL = valueL
        if (prev_valueR == valueR or prev_valueL == valueL) and hold_switch:
            msg = Float32MultiArray()
            rospy.loginfo(str(valueR) + " " + str(valueL))
            msg.data=[valueR, valueL]
            pub.publish(msg)
            '''
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 4:
                    hold_switch = False
                    prev_valueA = 0.0
                    prev_valueB = 0.0
            if event.type == pygame.JOYBUTTONDOWN: # changes the kill-switch value
                if event.button == 4:
                    hold_switch = True
            if event.type == pygame.JOYHATMOTION:
                if event.hat == 0:
                    interval+=event.value[1]*20
            if event.type == pygame.JOYAXISMOTION and hold_switch:
                if event.axis == 4:
                    valueA = 1*round(event.value, 1)*interval
                    prev_valueA = valueA
                if event.axis == 1:
                    valueB = -1*round(event.value, 1)*interval
                    prev_valueB = valueB
        if (prev_valueA == valueA or prev_valueB == valueB) and hold_switch:
            msg = Float32MultiArray()
            rospy.loginfo(str(valueA) + " " + str(valueB))
            msg.data=[valueA, valueB]
            pub.publish(msg)
        '''
        rate.sleep()
        
  
    


if __name__=='__main__':
    pygame.init()  # initialize pygame module
    pygame.joystick.init()  # initialize joystick module
    
    joystick1 = pygame.joystick.Joystick(0)  # create a joystick object for the first joystick
    joystick1.init()  # initialize the joystick object
    msg = Float32MultiArray()
    rospy.init_node("logi_controller")
    rospy.loginfo("logi_controller node has been started")

    pub = rospy.Publisher("/drive_vel", Float32MultiArray, queue_size=10)
    rate = rospy.Rate(10)
    
    try:
        controller_input()
    except rospy.ROSInterruptException:
        pass

if rospy.is_shutdown():
    pygame.quit()