import os
import time
import mysql.connector
import RPi.GPIO as GPIO

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

p.start(15) 
temp1=0

db = mysql.connector.connect(
	host="localhost",
	user="temp_logger",
	passwd="abc@123",
	database= "temperature"
	)
mycursor=db.cursor()
sql ="""INSERT INTO Temp_log (Temperature,RPM) VALUES (%s,%s)"""

def measure_temp():
	temp  = os.popen("vcgencmd measure_temp").readline()
	return (temp.replace("temp=","").replace("'C\n",""))

while True:
	
	temp1 =measure_temp()
	temp2=float(temp1)
	#print(temp1)
	
	
	if 35>temp2>30:
                print("run")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
		speed =15
        elif 40>temp2>35:
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
		p.ChangeDutyCycle(50)
		speed = 50
        elif temp2>40:
		GPIO.output(in1,GPIO.HIGH)
		GPIO.output(in2,GPIO.LOW)
		p.ChangeDutyCycle(80)
		speed = 80
	
	sql_temp = (temp1,speed,)
	mycursor.execute(sql,sql_temp)
	db.commit()
	time.sleep(5)
GPIO.cleanup()
