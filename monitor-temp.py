import os
import time
import mysql.connector 

db = mysql.connector.connect(
	host="localhost",
	user="temp_logger",
	passwd="abc@123",
	database= "temperature"
	)
mycursor=db.cursor()
sql ="""INSERT INTO Temp_log (Temperature) VALUES (%s)"""

temp1=0
def measure_temp():
	temp  = os.popen("vcgencmd measure_temp").readline()
	return (temp.replace("temp=","").replace("'C\n",""))

while True:
	time.sleep(1)
	temp1 =measure_temp() 
	print(temp1)
	sql_temp=(temp1,)
	mycursor.execute(sql,sql_temp)
	db.commit()
