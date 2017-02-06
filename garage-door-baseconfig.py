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
def move_door(doornum):
    doornum.toggle()
    sleep(.1)
    doornum.toggle()

# Check to see if the door is up for too long
def check_door(doornum): 
    if doornum.is_active==False:
        print("Door has been up for %i seconds" % doornum.inactive_time)
        if doornum.inactive_time > 3600:
            message = "Door %s has been up over an hour" % doornum
        else:
            return
    else:
        print("Door is closed")

check_door(sensor1)
check_door(sensor2)
move_door(relay1)
move_door(relay2)

# Clean up before exiting
def cleanup():
    relay1.close()
    relay2.close()
    sensor1.close()
    sensor2.close()

