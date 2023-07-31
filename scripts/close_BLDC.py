from Phidget22.Phidget import *
from Phidget22.Devices.BLDCMotor import *
import time

def main():
	bldcMotor0 = BLDCMotor()
	bldcMotor1 = BLDCMotor()
	bldcMotor0.setDeviceSerialNumber(683092)
	bldcMotor1.setDeviceSerialNumber(683092)
	bldcMotor0.setHubPort(3)
	bldcMotor1.setHubPort(2)
	time.sleep(1)
	bldcMotor0.close()
	bldcMotor1.close()
	
	time.sleep(1)
	'''
	bldcMotor0.setDeviceSerialNumber(683092)
	bldcMotor0.openWaitForAttachment(5000)
	bldcMotor0.close()
	
	
	bldcMotor1.setDeviceSerialNumber(683092)
	bldcMotor1.openWaitForAttachment(5000)
	bldcMotor1.close()
	'''

main()