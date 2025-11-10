
# deepsleep to system reset.

Touch Pin4 to GND.

```
$ mpr mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyUSB0
Use Ctrl-] or Ctrl-x to exit this shell
MicroPython v1.27.0-preview.317.g9999553aae.kaki5 on 2025-11-10; ESP32C3 AiTK KAKI5 with ESP32C3
>>> import deep_sleep_wakeon
Fresh boot
Going to deep sleep. Press button on GPIO4 to wake.
ESP-ROM:esp32c3-api1-20210207
Build:Feb  7 2021
rst:0x5 (DSLEEP),boot:0xc (SPI_FAST_FLASH_BOOT)
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fcd5820,len:0xddc
load:0x403cbf10,len:0x9ac
load:0x403ce710,len:0x2cb8
entry 0x403cbf10
MicroPython v1.27.0-preview.317.g9999553aae.kaki5 on 2025-11-10; ESP32C3 AiTK KAKI5 with ESP32C3
>>> from machine import RTC
>>> rtc = RTC()
>>> state = rtc.memory()
>>> state
b'woke'
```

# lightsleep wakeon pin interrupt.
 
Touch Pin4 to GND.

```
$ mpr mount .
Local directory . is mounted at /remote
Connected to MicroPython at /dev/ttyUSB0
Use Ctrl-] or Ctrl-x to exit this shell
>
MicroPython v1.27.0-preview.317.g9999553aae.kaki5 on 2025-11-10; ESP32C3 AiTK KAKI5 with ESP32C3
>>> import light_sleep_wakeon
Going to light sleep
Woke up
Going to light sleep
Woke up
Going to light sleep
Woke up
Going to light sleep
Woke up
Going to light sleep
...
```
