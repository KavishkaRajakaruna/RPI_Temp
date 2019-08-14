import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)

p.start(20)

while(1):
	
	x=raw_input()
	
	if x=='r':
		print("run")
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
	elif x=='l':
		print("Low")
		p.ChangeDutyCycle(50);
	elif x=='e':
		GPIO.cleanup()
		print("GPIO Cleanup")
