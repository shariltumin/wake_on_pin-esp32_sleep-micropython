import esp32
from machine import Pin, RTC, deepsleep, reset_cause, DEEPSLEEP_RESET
from time import sleep

rtc = RTC()

# Read persisted data from RTC memory, decode to string for demo
state = rtc.memory()
if state == b'woke':
    print("Woke up from deep sleep")
else:
    print("Fresh boot")

# Save the state back for next wakeup cycle
rtc.memory(b'woke')

# Configure pin 4 as input with pull-up for external wake
# hold=True is a must for S2 and S3
wake_pin = Pin(4, mode=Pin.IN, pull=Pin.PULL_UP, hold=True)
esp32.wake_on_ext0(pin=wake_pin, level=esp32.WAKEUP_ALL_LOW)

print("Going to deep sleep. Press button on GPIO4 to wake.")

sleep(2)  # Allow time to read messages

# Enter deep sleep, will reset CPU on wake
deepsleep()


