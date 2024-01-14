import umqtt_robust2 as mqtt
from machine import Pin
from neopixel import NeoPixel

n = 12
p = 26
np = NeoPixel(Pin(p, Pin.OUT), n)

class States:
    test_state = False

brightness = 255 

try:
    while True:
        if mqtt.besked:
            if isinstance(mqtt.besked, bytes):
                besked = mqtt.besked.decode('utf-8') 
            else:
                besked = mqtt.besked
            print("Lysstyrke modtaget:", besked)

            if besked == "start test state":
                print("Starter test state mode")
                States.test_state = True
            elif besked == "stop test state":
                print("Stopper test state mode")
                States.test_state = False
            elif besked.isdigit():
                brightness = int(besked)
                print("Ændret lysstyrke:", brightness)

            mqtt.besked = None

        mqtt.sync_with_adafruitIO()

        for i in range(n):
            np[i] = (brightness, brightness, brightness)
        np.write()

except KeyboardInterrupt:
    print("CTRL-C blev trykket...afslutter")
    server_socket.close()
    mqtt.c.cdisconnect()
    mqtt.sys.exit()
