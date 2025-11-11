# lightsleep_wakeontouch.py
#
import esp32
from machine import TouchPad, Pin, lightsleep
from time import sleep

touch_pin = TouchPad(Pin(4))
touch_pin.config(400)

esp32.wake_on_touch(True)

print("Going to light sleep. Touch Pin4 to wake.")
sleep(2)

lightsleep()

print("Woke up from light sleep")

