import umqtt_robust2 as mqtt
from machine import Pin, ADC
from time import sleep_ms
from neopixel import NeoPixel
from machine import Pin

# Højere bitantal øger følsomhed og nøjagtighed - Jeg bruger 9 bit her, istedet for 12
pot = ADC(Pin(34, Pin.IN), atten=3)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_9BIT)
led1 = Pin(26, Pin.OUT, value=0)

n = 12
p = 26
np = NeoPixel(Pin(p, Pin.OUT), n)

def mit_loop(delay_ms):
    for i in range(n):
        np[i] = (181, 168, 155)  
        np.write()
        sleep_ms(delay_ms)
        np[i] = (0, 0, 0)  

while True:
    pot_val = pot.read()
    spaending = pot_val * (3.3 / 4096)
    print("Analog potentiometer vaerdi:      ", pot_val)
    print("/nAnalog potentiometer spaending:      ", spaending)
    led1.value(not led1.value())

    mit_loop(pot_val)

    try:
        if len(mqtt.besked) != 0:
            mqtt.besked = ""
        mqtt.sync_with_adafruitIO()
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()

