# ESP32 WakeOn from Sleep using Pin interrupt

As part of a power-saving strategy, we can put the ESP32 into **deepsleep** and **lightsleep**. Here is an implementation of wake-on-pin interrupt from both deepsleep and lightsleep. The deepsleep wakes to a system power-on reset and lightsleep continues with the next statement after waking up.

Tests were run on ESP32 and ESP32-C3. The results were positive. Please have a look in the tests directory for the test scripts.

There are two files under ports/esp32 that need to be modified: 1) machine_pin.c and 2) modmachine.c.

With unmodified machine_pin.c:

```
>>> from machine import Pin
>>> Pin.
value           DRIVE_0         DRIVE_1         DRIVE_2
DRIVE_3         IN              IRQ_FALLING     IRQ_RISING
OPEN_DRAIN      OUT             PULL_DOWN       PULL_UP
WAKE_HIGH       WAKE_LOW        board           init
irq             off             on              toggle
```

With the modified machine_pin.c:
```
>>> from machine import Pin
>>> Pin.
value           DRIVE_0         DRIVE_1         DRIVE_2
DRIVE_3         IN              IRQ_FALLING     IRQ_HIGH_LEVEL
IRQ_LOW_LEVEL   IRQ_RISING      OPEN_DRAIN      OUT
PULL_DOWN       PULL_UP         WAKE_HIGH       WAKE_LOW
board           disable         enable          init
irq             off             on              toggle
```

There is something new here: 1)IRQ_HIGH_LEVEL, 2) IRQ_LOW_LEVEL, 3) disable and 4) enable.

For ESP32-C3 firmware is built without the SOC_PM_SUPPORT_EXT0_WAKEUP flag, the esp32.wake_on_ext0() will not be defined.

Without SOC_PM_SUPPORT_EXT0_WAKEUP:
```
>>> import esp32
>>> esp32.
HEAP_DATA       HEAP_EXEC       NVS             Partition
RMT             WAKEUP_ALL_LOW  WAKEUP_ANY_HIGH
gpio_deep_sleep_hold            idf_heap_info   mcu_temperature
```

With the flag set:
```
>>> import esp32
>>> esp32.
HEAP_DATA       HEAP_EXEC       NVS             Partition
RMT             WAKEUP_ALL_LOW  WAKEUP_ANY_HIGH
gpio_deep_sleep_hold            idf_heap_info   mcu_temperature
wake_on_ext0
```

We need the ```esp32.wake_on_ext0()``` function. It is necessary for the deepsleep wake-on-pin interrupt to function.

