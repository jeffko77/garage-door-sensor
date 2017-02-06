# Python3

"""
Primary Pins in use on this config
	Left Door Relay - Pin 21 (Yellow Wire)
	Left Door Sensor - Pin 5 (Purple Wire)
	Right Door Relay - Pin 16(Orange Wire)
	Right Door Sensor - Pin 7(Green Wire)
"""

# Base functions are all from gpiozero

import gpiozero
from time import sleep

relay1 = gpiozero.OutputDevice(21,True,True)
sensor1 = gpiozero.DigitalInputDevice(5,True,None)
relay2 = gpiozero.OutputDevice(16,True,True)
sensor2 = gpiozero.DigitalInputDevice(7,True,None)


# Open/Close the Door by cycling the relay
def moveDoor(doornum)
    relay+str(doornum).toggle()
    sleep(.1)
    relay+str(doornum).toggle()

# Check to see if the door is up for too long
def checkDoor(doornum)
    door = sensor+str(doornum)
    