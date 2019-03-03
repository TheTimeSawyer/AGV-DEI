#Python code for Forward and Backward movement of the AGV. To be run on Raspberry Pi.
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
p = GPIO.PWM(17, 100)

#The forw() function as the name suggests gives the command for forwarding the vehicle.
def forw():
      p.start(50)

#The rev() function as the name suggests gives the command for reversing the vehicle.
def rev():
      GPIO.setup(17,GPIO.LOW)
      GPIO.output(18,GPIO.HIGH)
      p.start(70)
      
#The stop() function is used to stop the vehicle. In order to override any of the other functions call stop().
def stop():
      p.ChangeDutyCycle(10)
      
#This is for the honking. Added to support pedestrian detection.
def beep():
      GPIO.output(18,GPIO.HIGH)
