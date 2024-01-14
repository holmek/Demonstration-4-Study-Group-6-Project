from machine import Pin, ADC
from neopixel import NeoPixel
from time import sleep_ms

pot = ADC(Pin(34, Pin.IN), atten=3)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_9BIT)
led1 = Pin(26, Pin.OUT, value=0)

n = 12
p = 26
np = NeoPixel(Pin(p, Pin.OUT), n)

button_pin = Pin(4, Pin.IN)
button_last_state = 1
button_last_change_time = None  

class States:
    test_state = False
    last_printed_state = None

brightness = 255
led_index = 0
delay_ms = 100

try:
    while True:
        button_state = button_pin.value()
        current_time = sleep_ms(1) 

        if button_state == 0 and button_last_state == 1 and (button_last_change_time is None or (current_time - button_last_change_time) > 200):
            States.test_state = not States.test_state
            if not States.test_state:
                delay_ms = 100
            button_last_change_time = current_time

        button_last_state = button_state

        if States.test_state and States.last_printed_state != "aktiv":
            print("State er aktiv")
            States.last_printed_state = "aktiv"
        elif not States.test_state and States.last_printed_state != "ikke aktiv":
            print("State er inaktiv")
            States.last_printed_state = "ikke aktiv"

        if States.test_state:
            pot_value = pot.read()
            led_index = int((pot_value / 511.0) * n)

        for i in range(n):
            if i == led_index:
                np[i] = (brightness, brightness, brightness)
            else:
                np[i] = (0, 0, 0)
        np.write()

except KeyboardInterrupt:
    print("CTRL-C blev trykket...afslutter")