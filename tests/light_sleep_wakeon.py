from machine import Pin, lightsleep, SLEEP
from time import sleep_ms

def isr(pin):
#    print("Interrupt detected on", pin)
    pin.disable()  # Disable interrupt immediately on wakeup

pa = Pin(4, Pin.IN, Pin.PULL_UP)
pa.irq(trigger=Pin.IRQ_LOW_LEVEL, wake=SLEEP, handler=isr)

while True:
    print("Going to light sleep")
    sleep_ms(100)  # Pause to flush prints
    lightsleep()
    print("Woke up")
    pa.enable()    # Re-enable interrupt for next wake event
    sleep_ms(500)

