import pygame
import RPi.GPIO as GPIO
import time

pygame.mixer.init()
beep = pygame.mixer.Sound("Beep.wav") #inserts Beep.wav into program



print("Distance Measurement In Progress")


print ("Waiting For Sensor To Settle")
time.sleep(2)
while True:
    GPIO.setmode(GPIO.BCM)
    TRIG = 23
    ECHO = 24 #indicates the GPIO ID of TRIG and ECHO

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN) #sets GPIO input and output


    GPIO.output(TRIG, False)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False) #fires ultrasound pulse
    print("Settling finished")
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        print("Pulse_start",pulse_start) #store the time the pulse is fired
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        print("Pulse_end",pulse_end) #store the time the pulse returns
    pulse_duration = pulse_end - pulse_start #calculate time for pulse to fire, reflect off object, then return

    distance = pulse_duration * 17150 #Calculates distance in cm with distance #speed*time/2

    distance = round(distance, 2) #rounds distance by 2d.p.
    
    def output():
        print("Distance:", distance, "cm")
        beep.play() #function for printing distance and playing the sound (the print is for testing)
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
        beep.stop() #sleep time changes depending on the distance between device and object. Up to 1m. After time ends, the sound ends.

    else:
        print("Nothing in range")#if nothing is in range, do not play sound

    GPIO.cleanup() #cleans GPIO for next loop
    time.sleep(0.1)

