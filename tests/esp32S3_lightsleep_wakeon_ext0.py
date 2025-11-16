from machine import Pin, lightsleep
from time import sleep_ms
import esp32

# Use an RTC-capable pin on the S3 - GPIO1, GPII10
trigger = 10 # 1, 10
# hold=True parameter is critical!
wake_pin = Pin(trigger, Pin.IN, Pin.PULL_UP, hold=True)  
esp32.wake_on_ext0(pin=wake_pin, level=esp32.WAKEUP_ALL_LOW)

while True:
    print(f"Going to light sleep. Touch Pin{trigger} to GND to wake up")
    sleep_ms(200)  # Pause to flush prints
    lightsleep()
    print("Woke up")
    sleep_ms(500)

