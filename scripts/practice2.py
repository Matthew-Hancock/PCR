from Phidget22.Phidget import *
from Phidget22.Devices.MotorPositionController import *
import pygame  # import pygame module
import time
import math

# global properties:
# intialize motor properties
#motorPositionController0 = MotorPositionController()
#motorPositionController1 = MotorPositionController()
#motorPositionController0.setHubPort(0)
#motorPositionController1.setHubPort(1)
#motorPositionController0.setDeviceSerialNumber(683092)
#motorPositionController1.setDeviceSerialNumber(683092)
#motorPositionController0.openWaitForAttachment(5000)
#motorPositionController1.openWaitForAttachment(5000)
#motorPositionController0.setEngaged(True)
#motorPositionController1.setEngaged(True)
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
def do_more_stuff(valueR, valueL):
    positionR = motorPositionController0.getPosition()
    positionL = motorPositionController1.getPosition()
    print("current positionR: {} target position: {}".format(positionR,valueR+positionR))
    print("current positionL: {} target position: {}".format(positionL, valueL + positionL))
    motorPositionController0.setTargetPosition(valueR + positionR)
    motorPositionController1.setTargetPosition(valueL + positionL)

def do_stuff():
    valueR = 0
    valueL = 0
    prev_valueR = 0  # variable to keep track of previous value
    prev_valueL = 0
    done = False
    hold_switch = False
    interval = 100
    while not done:
        for event in pygame.event.get():
            print(event)
            #if event.type == pygame.JOYDEVICEREMOVED or (event.type == pygame.JOYBUTTONUP and event.button == 2):  # if user quits
                #done = True
            if event.type == pygame.JOYBUTTONUP and event.button == 4:
                hold_switch = False
                prev_valueR = 0
                prev_valueL = 0
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 4:
                hold_switch = True
            if event.type == pygame.JOYHATMOTION and event.hat == 0:
                interval += event.value[1] * 20
            if event.type == pygame.JOYAXISMOTION and hold_switch:
                if event.axis == 4:
                    valueR = -round(event.value, 1)*interval
                    prev_valueR = valueR
                elif event.axis == 1:
                    valueL = round(event.value, 1)*interval
                    prev_valueL = valueL
        if (prev_valueR == valueR or prev_valueL == valueL) and hold_switch:
            print(valueR, valueL)
        time.sleep(0.1)
            
            #do_more_stuff(valueR,valueL)
do_stuff()


#motorPositionController0.close()
#motorPositionController1.close()
