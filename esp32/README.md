
You need to build your MicroPython firmware using these modified files to implement the wake-on-pin interrupt from deepsleep and lightsleep.

machine_pin.c:

```
$ diff machine_pin.c machine_pin.c-ORIG
10,11d9
<  * Edited 2025 Sharil Tumin
<  *
306c304
<         { MP_QSTR_trigger, MP_ARG_INT, {.u_int = GPIO_INTR_POSEDGE | GPIO_INTR_NEGEDGE | GPIO_INTR_LOW_LEVEL | GPIO_INTR_HIGH_LEVEL} },
---
>         { MP_QSTR_trigger, MP_ARG_INT, {.u_int = GPIO_INTR_POSEDGE | GPIO_INTR_NEGEDGE} },
373,390d370
< // Disable interrupts for the pin
< static mp_obj_t machine_pin_disable(mp_obj_t self_in) {
<     machine_pin_obj_t *self = MP_OBJ_TO_PTR(self_in);
<     gpio_num_t index = PIN_OBJ_PTR_INDEX(self);
<     gpio_intr_disable(index);
<     return mp_const_none;
< }
< static MP_DEFINE_CONST_FUN_OBJ_1(machine_pin_disable_obj, machine_pin_disable);
< 
< // Enable interrupts for the pin
< static mp_obj_t machine_pin_enable(mp_obj_t self_in) {
<     machine_pin_obj_t *self = MP_OBJ_TO_PTR(self_in);
<     gpio_num_t index = PIN_OBJ_PTR_INDEX(self);
<     gpio_intr_enable(index);
<     return mp_const_none;
< }
< static MP_DEFINE_CONST_FUN_OBJ_1(machine_pin_enable_obj, machine_pin_enable);
< 
406,407d385
<     { MP_ROM_QSTR(MP_QSTR_enable), MP_ROM_PTR(&machine_pin_enable_obj) },
<     { MP_ROM_QSTR(MP_QSTR_disable), MP_ROM_PTR(&machine_pin_disable_obj) },
420,423d397
< //    { MP_ROM_QSTR(MP_QSTR_IRQ_LOW_LEVEL), MP_ROM_INT(ESP_GPIO_INTR_LOW_LEVEL) },
< //    { MP_ROM_QSTR(MP_QSTR_IRQ_HIGH_LEVEL), MP_ROM_INT(ESP_GPIO_INTR_HIGH_LEVEL) },
<     { MP_ROM_QSTR(MP_QSTR_IRQ_LOW_LEVEL), MP_ROM_INT(GPIO_INTR_LOW_LEVEL) },
<     { MP_ROM_QSTR(MP_QSTR_IRQ_HIGH_LEVEL), MP_ROM_INT(GPIO_INTR_HIGH_LEVEL) },
```

modmachine.c:
```
$ diff modmachine.c modmachine.c-ORIG
11,12d10
<  * Edited 2025 Sharil Tumin
<  *
147,150d144
< 	#if CONFIG_IDF_TARGET_ARCH_RISCV
< 	esp_deep_sleep_enable_gpio_wakeup(1ULL << machine_rtc_config.ext0_pin, machine_rtc_config.ext0_level ? 1 : 0);
< 
<         #else
152d145
<         #endif
182,189d174
< 	    #if SOC_PM_SUPPORT_EXT0_WAKEUP
< 	    gpio_num_t wake_pin = machine_rtc_config.ext0_pin;
<             int wake_level = machine_rtc_config.ext0_level;
<             if (wake_pin != -1) {
<                 gpio_wakeup_enable(wake_pin, wake_level ? GPIO_INTR_HIGH_LEVEL : GPIO_INTR_LOW_LEVEL);
<                 esp_sleep_enable_gpio_wakeup();
<             }
< 	    #endif
```

You also need to set the SOC_PM_SUPPORT_EXT0_WAKEUP flag in boards/MYBORD/mpconfigboard.h (at least for ESP32-C3, a RISCV-based MCU).

I build my ESP32-XX firmwares using ESP-IDF-V5.5.1
