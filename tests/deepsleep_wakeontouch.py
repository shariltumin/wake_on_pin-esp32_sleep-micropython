# deepsleep_wakeontouch.py
#
import esp32
from machine import TouchPad, Pin, deepsleep
from time import sleep

touch_pin = TouchPad(Pin(4))   # Use touch capable pin, e.g., GPIO4
touch_pin.config(400)          # Set touch threshold; adjust for sensitivity

esp32.wake_on_touch(True)      # Enable touch wakeup source

print("Going to deep sleep. Touch the pad to wake.")
sleep(2)

deepsleep()

