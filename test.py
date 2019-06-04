import webiopi
import datetime
 
GPIO = webiopi.GPIO
 
IN1 = 17 # GPIO pin using BCM numbering
IN2 = 4

 
def setup():
	GPIO.setFunction(IN1, GPIO.OUT)
	GPIO.setFunction(IN2, GPIO.OUT)

def loop():
	#if (GPIO.digitalRead(IN1) == GPIO.LOW):
		#GPIO.digitalWrite(IN1, GPIO.HIGH)
		#GPIO.digitalWrite(IN2, GPIO.LOW)
 
	#if (GPIO.digitalRead(IN1) == GPIO.HIGH):
		#GPIO.digitalWrite(IN1, GPIO.LOW)
		#GPIO.digitalWrite(IN2, GPIO.HIGH)
 
	#webiopi.sleep(1)

@webiopi.macro
def moveForward():
	GPIO.digitalWrite(IN1, GPIO.HIGH);
	GPIO.digitalWrite(IN2, GPIO.LOW);
 
def destroy():
	GPIO.digitalWrite(IN1, GPIO.LOW)
	GPIO.digitalWrite(IN2, GPIO.LOW)
