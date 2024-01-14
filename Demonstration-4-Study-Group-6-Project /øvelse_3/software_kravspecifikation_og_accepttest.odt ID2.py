from machine import Pin
from time import sleep_ms
from neopixel import NeoPixel

n = 12
p = 26
np = NeoPixel(Pin(p, Pin.OUT), n)

button_pin = Pin(4, Pin.IN)

led_index = 0
delay_ms = 100

def loop1():
    for i in range(n):
        if i == led_index:
            np[i] = (181, 168, 155)
        else:
            np[i] = (0, 0, 0)
    np.write()

while True:
    if not button_pin.value():
        led_index = (led_index + 1) % n

    loop1()
    sleep_ms(delay_ms)