import webiopi
GPIO = webiopi.GPIO

IN1 = 2
IN2 = 3
IN3 = 4
IN4 = 17

LeftMotor =  [IN1, IN2]
RightMotor = [IN3, IN4]

def setup():
	webiopi.debug("setup")

	GPIO.setFunction(IN1, GPIO.OUT)
	GPIO.setFunction(IN2, GPIO.OUT)
	GPIO.setFunction(IN3, GPIO.OUT)
	GPIO.setFunction(IN4, GPIO.OUT)

def loop():
	webiopi.sleep(0.1)

def destroy():
	GPIO.digitalWrite(IN1, GPIO.LOW)
	GPIO.digitalWrite(IN2, GPIO.LOW)
	GPIO.digitalWrite(IN3, GPIO.LOW)
	GPIO.digitalWrite(IN4, GPIO.LOW)

@webiopi.macro
def stop():
	GPIO.digitalWrite(LeftMotor[0], GPIO.LOW)
	GPIO.digitalWrite(LeftMotor[1], GPIO.LOW)
	GPIO.digitalWrite(RightMotor[0], GPIO.LOW)
	GPIO.digitalWrite(RightMotor[1], GPIO.LOW)

@webiopi.macro
def forward():
	#webiopi.debug("forward");

	GPIO.digitalWrite(LeftMotor[0], GPIO.HIGH)
	GPIO.digitalWrite(LeftMotor[1], GPIO.LOW)
	GPIO.digitalWrite(RightMotor[0], GPIO.HIGH)
	GPIO.digitalWrite(RightMotor[1], GPIO.LOW)

@webiopi.macro
def back():
	#webiopi.debug("reverse");

	GPIO.digitalWrite(LeftMotor[0], GPIO.LOW)
	GPIO.digitalWrite(LeftMotor[1], GPIO.HIGH)
	GPIO.digitalWrite(RightMotor[0], GPIO.LOW)
	GPIO.digitalWrite(RightMotor[1], GPIO.HIGH)

@webiopi.macro
def left():
	GPIO.digitalWrite(LeftMotor[0], GPIO.LOW)
	GPIO.digitalWrite(LeftMotor[1], GPIO.HIGH)
	GPIO.digitalWrite(RightMotor[0], GPIO.HIGH)
	GPIO.digitalWrite(RightMotor[1], GPIO.LOW)

@webiopi.macro
def right():
	GPIO.digitalWrite(LeftMotor[0], GPIO.HIGH)
	GPIO.digitalWrite(LeftMotor[1], GPIO.LOW)
	GPIO.digitalWrite(RightMotor[0], GPIO.LOW)
	GPIO.digitalWrite(RightMotor[1], GPIO.HIGH)




