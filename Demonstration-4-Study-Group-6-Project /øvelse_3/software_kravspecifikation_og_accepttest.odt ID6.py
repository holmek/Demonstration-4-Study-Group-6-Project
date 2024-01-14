from machine import Pin, PWM
from socket import socket, AF_INET, SOCK_DGRAM
from sys import exit
import random
from time import sleep

BUZZ_PIN = 23
buzzer_pin = Pin(BUZZ_PIN, Pin.OUT)
pwm_buzz = PWM(buzzer_pin)

def buzzer(buzzer_PWM_object, frequency, sound_duration, silence_duration):
    buzzer_PWM_object.duty(512)
    buzzer_PWM_object.freq(frequency)
    sleep(sound_duration)
    buzzer_PWM_object.duty(0)
    sleep(silence_duration)

buzzer(pwm_buzz, 262, 0.2, 0.2)
buzzer(pwm_buzz, 294, 0.4, 0.3)

def spil_random_toner():
    tones = [261, 293, 329, 349, 392, 440]  
    for _ in range(3):
        tone = random.choice(tones)  
        buzzer(pwm_buzz, tone, 0.2, 0.2) 

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("", server_port))
print("Serveren er klar til at modtage")

try:
    while True:
        besked, klientadresse = server_socket.recvfrom(2048)
        ændret_besked = besked.decode()
        server_socket.sendto(ændret_besked.encode(), klientadresse)

        if ændret_besked == "spil random toner":
            spil_random_toner()

        if ændret_besked != "":
            print(ændret_besked)

except KeyboardInterrupt:
    print("CTRL-C er blevet trykket, afslutter!")
    server_socket.close()

