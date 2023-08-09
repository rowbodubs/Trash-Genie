import RPi.GPIO as GPIO
from time import sleep


def setVert(angle):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	pwm=GPIO.PWM(18, 50)
	pwm.start(0)

	duty = angle / 18 + 3
	GPIO.output(18, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(18, False)
	pwm.ChangeDutyCycle(duty)
	pwm.stop()
	GPIO.cleanup()
	
def setHorz(angle):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
	pwm=GPIO.PWM(17, 50)
	pwm.start(0)
	
	duty = angle / 18 + 3
	GPIO.output(17, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(17, False)
	pwm.ChangeDutyCycle(duty)
	pwm.stop()
	GPIO.cleanup() 

def center():
    setVert(115)
    setHorz(27)
    
def paper():
	#setHorz(0)
    setHorz(160)
    #setVert(0)
    setVert(20)
    center()

def plastic():
    setHorz(55)
    #setVert(0)
    setVert(20)
    center()

def trash():
    #setHorz(170)
    setHorz(120)
    #setVert(175)
    setVert(174)
    center()
    
def dump(detection):
    if detection == "CLOTH" or detection == "BIODEGRADABLE":
        trash()
    elif detection == "PLASTIC" or detection == "METAL" or detection == "GLASS":
        plastic() 
    elif detection == "PAPER" or detection == "CARDBOARD":
        paper()
    
#center()
#trash()
#metals()
#plastic()
dump("CLOTH")
dump("PLASTIC")
dump("PAPER")
#setHorz(60)
#setVert(20)

