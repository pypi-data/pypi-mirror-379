"""Usage examples of the MyRIO class: MXP board tests

This examples show how to use the electronic components
we already have on our MXP boards. It serves as example of
more sophisticated functions we added to myRIO_base.

Our MXP cards have an RGB LED connected to DIO_2:0 and
two push buttons on DIO_4:3. We also have an NTC temperature
sensor in AI0 and an LDR light sensor in AI1. We use these
channels in our examples. The port that we use most is the
A port, so we set it as default on our package.

Last update: 2024/03/14 Aitzol Ezeiza Ramos (UPV/EHU)
"""

import myRIO_base as myRIO
from time import sleep

myrio1 = myRIO.MyRIO()

print("Read temperature from MXP port A, channel 0:")
print(myrio1.read_MXP_temperature())
print("Push the first button to continue (DIO3)")
while not (myrio1.read_MXP_button(1)):
    sleep(0.1)
print("Read luminosity from MXP port A, channel 1:")
print(myrio1.read_MXP_luminosity())
print("Push the second button to continue (DIO4)")
while not (myrio1.read_MXP_button(2)):
    sleep(0.1)
print("RGB LED in MXP port A: RED")
myrio1.write_MXP_RGB_LED(myRIO.RED)
sleep(1)
print("RGB LED in MXP port A: GREEN")
myrio1.write_MXP_RGB_LED(myRIO.GREEN)
sleep(1)
print("RGB LED in MXP port A: BLUE")
myrio1.write_MXP_RGB_LED(myRIO.BLUE)
sleep(1)
print("RGB LED in MXP port A: OFF")
myrio1.write_MXP_RGB_LED(myRIO.RGB_OFF)
