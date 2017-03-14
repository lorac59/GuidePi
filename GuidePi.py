import pygame
import RPi.GPIO as GPIO
import time
import math
import pyaudio

pygame.mixer.init()
beep = pygame.mixer.Sound("Beep.wav")



print("Distance Measurement In Progress")


print ("Waiting For Sensor To Settle")
time.sleep(2)
while True:
    GPIO.setmode(GPIO.BCM)
    TRIG = 23
    ECHO = 24

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)


    GPIO.output(TRIG, False)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    print("Settling finished")
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        print("Pulse_start",pulse_start)
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        print("Pulse_end",pulse_end)
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    
    def output():
        print("Distance:", distance, "cm")
        beep.play()
    if distance <2:
        output()
        time.sleep(0)
        beep.stop()
    elif distance >2 and distance < 30:
        output()
        time.sleep(.5)
        beep.stop()
    elif distance >30 and distance < 50:
        output()
        time.sleep(0.8)
        beep.stop()
    elif distance >50 and distance < 100:
        output()
        time.sleep(2)
        beep.stop()

    else:
        print("Nothing in range")

    GPIO.cleanup()
    time.sleep(0.1)

