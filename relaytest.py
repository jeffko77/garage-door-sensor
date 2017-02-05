import gpiozero
from time import sleep

relay1 = gpiozero.OutputDevice(21,True,True)
#relay1.high()
relay1.toggle()
sleep(.1)
relay1.toggle()


