import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)
GPIO.output(19,GPIO.HIGH)
p = GPIO.PWM(17, 100)

def forw():
    p.start(50)
          
def rev():
    GPIO.output(17,GPIO.LOW)
    time.sleep(1)
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)
    p.start(70)
        
def stop():
    p.ChangeDutyCycle(10)
    GPIO.output(18,GPIO.HIGH)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)

def beep():
    GPIO.output(18,GPIO.LOW)

def left():
    GPIO.output(13,GPIO.LOW)
    time.sleep(0.20)
    GPIO.output(13,GPIO.HIGH)

def right():
    GPIO.output(19,GPIO.LOW)
    time.sleep(0.20)
    GPIO.output(19,GPIO.HIGH)

def forwd(t):
    forw()
    time.sleep(t)
    stop()

def leftan(a):
      i=1
      while(i<=a) :
            i=i+1
            left()
            time.sleep(1)
def rightan(a):
      i=1
      while(i<=a) :
            i=i+1
            right()
            time.sleep(1)

def revd(t):
    rev()
    time.sleep(t+2)
    stop()
def Uturn(a,t,di):
    if(di=='r'):
        rightan(a)
        forwd(t)          
    if(di=='l'):
        leftan(a)
        forwd(t)
        

forwd(34.9)
leftan(3)
forwd(16.2)
rightan(4)
forwd(3)
forwd(105)
leftan(3)
forwd(16.2)
rightan(4)
forwd(3)



