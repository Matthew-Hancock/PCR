from Phidget22.Phidget import *
from Phidget22.Devices.MotorPositionController import *
import pygame  # import pygame module
import time
import math

# global properties:
# intialize motor properties
motorPositionController0 = MotorPositionController()
motorPositionController1 = MotorPositionController()
motorPositionController0.setHubPort(0)
motorPositionController1.setHubPort(1)
motorPositionController0.setDeviceSerialNumber(683092)
motorPositionController1.setDeviceSerialNumber(683092)
motorPositionController0.openWaitForAttachment(5000)
motorPositionController1.openWaitForAttachment(5000)
motorPositionController0.setEngaged(True)
motorPositionController1.setEngaged(True)
'''
motorPositionController0.setKp(60000)
m1 = motorPositionController0.getPositon()
m2 = motorPositionController0.getDataInterval()
m3 = motorPositionController0.getDataRate()
m4 = motorPositionController0.getDeadBand()
m5 = motorPositionController0.getKd()
m6 = motorPositionController0.getKp()
m7 = motorPositionController0.getKi()
m8 = motorPositionController0.getRescaleFactor()

print("Acceleration: {} Data Interval: {} Data Rate: {} Dead Band".format(m1,m2,m3,m4))
print("Kd: {} Kp: {} Ki: {} Rescale Factor".format(m5,m6,m7,m8))
'''
# first class: motor inputs
def do_more_stuff(valueA, valueB):
    positionA = motorPositionController0.getPosition()
    positionB = motorPositionController1.getPosition()
    print("current positionA: {} target position: {}".format(positionA,valueA+positionA))
    print("current positionB: {} target position: {}".format(positionB, valueB + positionB))
    motorPositionController0.setTargetPosition(valueA+positionA)
    motorPositionController1.setTargetPosition(valueB + positionB)

# takes in values from controller and executes commands


# second class: controller outputs
def do_stuff():
    # Do stuff with Phidgets here or in event handlers
    valueA=0
    valueB = 0
    pygame.init()  # initialize pygame module
    pygame.joystick.init()  # initialize joystick module
    joystick_count = pygame.joystick.get_count()  # get the number of joysticks
        
    joystick = pygame.joystick.Joystick(0)  # create a joystick object for the first joystick
    joystick.init()  # initialize the joystick object
    done = False
    prev_valueA = 0  # variable to keep track of previous value
    prev_valueB = 0
    hold_switch = False
    interval = 100
    while not done:
        for event in pygame.event.get():  # get pygame event
            if event.type == pygame.QUIT:  # if user quits
                done = True  # exit loop
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
            do_more_stuff(valueA,valueB)
do_stuff()
motorPositionController0.close()
motorPositionController1.close()
# while loop continously reads controller inputs and exports values to first class

# for loop gets values from controller

# adjusts or rounds the values from the input

# while value from joystick is greater than 0

# use the given value to increase the target position if the value increases or decrease the target position if the value decreases

# use the value to move the motor forward

# while value from joystick is less than 0

# use the given value to increase the target position if the value increases or decrease the target position if the value decreases

# use the value to move the motor backward

# while valye from joystick is equal to 0

# keep the target position equal to the given position

# sends values from controller to first class
