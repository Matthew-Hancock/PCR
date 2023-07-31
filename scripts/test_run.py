from Phidget22.Phidget import *
from Phidget22.Devices.BLDCMotor import *
import pygame # import pygame module
import time
import math
#Declare any event handlers here. These will be called every time the associated event occurs.

def do_stuff():

  #Create Phidget channels
  bldcMotor0 = BLDCMotor()
  

  #Set addressing parameters to specify which channel to open (if any)
  bldcMotor0.setHubPort(0)
  bldcMotor0.setDeviceSerialNumber(683092)
  

  #Assign any event handlers needed before calling open so that no events are missed.

  # Open your Phidgets and wait for attachment
  bldcMotor0.openWaitForAttachment(5000)
  
  minVelocity0 = bldcMotor0.getMinVelocity()
  
  bldcMotor0.setTargetBrakingStrength(1)
  


  #resetFailsafe() <- could be needed to reset the timer everytime it is in use


  # Do stuff with Phidgets here or in event handlers

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
            if event.button == 2: # if user quits
                done = True # exit loop
            if event.type == pygame.JOYBUTTONDOWN: # changes the kill-switch value
                if event.button == 4:
                    print("ON")
                    hold_switch = True
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 4:
                    print("OFF")
                    hold_switch = False
            if event.type == pygame.JOYAXISMOTION and hold_switch: # if user moves joysticks and has kill-switch pressed
                if event.axis == 1: # if it is the left stick's vertical axis
                    valueA = round(event.value, 2)*0.6 # get the value of the axis
                    bldcMotor0.setTargetVelocity(valueA) # set the target velocity of the motor to the value
                if event.axis == 3: # if it is the right stick's vertical axis
                    valueB = -round(event.value, 2)*0.6 # get the value of the axis (invert it because up is negative)
                #print(f"Target A velocity: {valueA}, B velocity: {valueB}")
            else:
                bldcMotor0.setTargetVelocity(minVelocity0)  # set the target velocity of the motor to the value
                #print(pygame.joystick.Joystick(0).get_power_level())
      
  pygame.quit()  # quit pygame module



  #Close your Phidgets once the program is done.
  #bldcMotor0.close()

try:
    do_stuff()
except:
    print("disconnected")