from machine import Pin, ADC
from time import sleep_ms
from neopixel import NeoPixel

def loop1():
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
        print("Analog potentiometer value: ", pot_val)
        print("\nAnalog potentiometer voltage: ", spaending)
        led1.value(not led1.value())

        delay_ms = int(pot_val / 10) 

        for i in range(n):
            np[i] = (181, 168, 155)
            np.write()
            sleep_ms(delay_ms)
            np[i] = (0, 0, 0)

loop1()

