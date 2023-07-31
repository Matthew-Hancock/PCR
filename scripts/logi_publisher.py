#!/usr/bin/python

import rospy
from std_msgs.msg import Float32MultiArray
import pygame

def controller_input():

  pygame.init() # initialize pygame module
  pygame.joystick.init() # initialize joystick module
  joystick_count = pygame.joystick.get_count() # get the number of joysticks
  
  joystick = pygame.joystick.Joystick(0) # create a joystick object for the first joystick
  joystick.init() # initialize the joystick object

  done = False # variable for loop
  hold_switch = False # variable for kill-switch
  valueA = 0 # variables for velocity values
  valueB = 0
  while not done:
      for event in pygame.event.get(): # get pygame event
           # if event.button == 2: # if user quits
               # done = True # exit loop
            if event.type == pygame.JOYBUTTONDOWN: # changes the kill-switch value
                if event.button == 4:
                    print("ON")
                    hold_switch = True
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 4:
                    print("OFF")
                    hold_switch = False
            if event.type == pygame.JOYAXISMOTION: #and hold_switch: # if user moves joysticks and has kill-switch pressed
                if event.axis == 1: # if it is the left stick's vertical axis
                    valueA = round(event.value, 2)*0.6 # get the value of the axis
                if event.axis == 4: # if it is the right stick's vertical axis
                    valueB = -round(event.value, 2)*0.6 # get the value of the axis (invert it because up is negative)
                #print(f"Target A velocity: {valueA}, B velocity: {valueB}")
            else:
                valueA = 0
                valueB = 0
      rospy.loginfo(hold_switch)
      msg = Float32MultiArray()
      msg.data=[valueA, valueB]
      pub.publish(msg)
  pygame.quit()  # quit pygame module



  #Close your Phidgets once the program is done.
  #bldcMotor0.close()

if __name__=='__main__':
    rospy.init_node("logi_controller")
    rospy.loginfo("logi_controller node has been started")

    pub = rospy.Publisher("/drive_vel", Float32MultiArray, queue_size=10)
    controller_input()
    rate = rospy.Rate(5)