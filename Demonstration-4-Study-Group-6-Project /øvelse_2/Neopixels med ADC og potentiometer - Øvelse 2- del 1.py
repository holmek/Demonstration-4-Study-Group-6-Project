import umqtt_robust2 as mqtt
from machine import Pin, ADC
from time import sleep_ms
from neopixel import NeoPixel
from machine import Pin

pot = ADC(Pin(34, Pin.IN), atten=3)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)
led1 = Pin(26, Pin.OUT, value=0)

n = 12
p = 26
np = NeoPixel(Pin(p, Pin.OUT), n)

while True:
    pot_val = pot.read()
    spaending = pot_val * (3.3 / 4096)
    print("Analog potentiometer vaerdi:      ", pot_val)
    print("/nAnalog potentiometer spaending:      ", spaending)
    led1.value(not led1.value())

    if pot_val < 500:
        for i in range(n):
            np[i] = (255, 0, 0)
    elif pot_val > 3000:
        for i in range(n):
            np[i] = (0, 255, 0) 
    else:
        for i in range(n):
            np[i] = (255, 255, 0)
    np.write()
    sleep_ms(pot_val)

    try:
        if len(mqtt.besked) != 0:
            mqtt.besked = ""
        mqtt.sync_with_adafruitIO()
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()