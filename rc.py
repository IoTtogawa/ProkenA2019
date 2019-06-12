import webiopi
GPIO = webiopi.GPIO

IN1 = 2
IN2 = 3
IN3 = 4
IN4 = 17

LeftMotor =  [IN1, IN2]
RightMotor = [IN3, IN4]

def setup():
	GPIO.setFunction(LeftMotor[0], GPIO.PWM)
	GPIO.setFunction(LeftMotor[1], GPIO.PWM)
	GPIO.setFunction(RightMotor[0], GPIO.PWM)
	GPIO.setFunction(RightMotor[1], GPIO.PWM)



def loop():
	webiopi.sleep(0.1)

def destroy():
	GPIO.pwmWrite(LeftMotor[0], 0)
	GPIO.pwmWrite(LeftMotor[1], 0)
	GPIO.pwmWrite(RightMotor[0], 0)
	GPIO.pwmWrite(RightMotor[1], 0)

@webiopi.macro
def stop():
	GPIO.pwmWrite(LeftMotor[0], 0)
	GPIO.pwmWrite(LeftMotor[1], 0)
	GPIO.pwmWrite(RightMotor[0], 0)
	GPIO.pwmWrite(RightMotor[1], 0)

@webiopi.macro
def forward():
	GPIO.pwmWrite(LeftMotor[0], 1)
	GPIO.pwmWrite(LeftMotor[1], 0)
	GPIO.pwmWrite(RightMotor[0], 1)
	GPIO.pwmWrite(RightMotor[1], 0)
@webiopi.macro
def back():
	GPIO.pwmWrite(LeftMotor[0], 0)
	GPIO.pwmWrite(LeftMotor[1], 1)
	GPIO.pwmWrite(RightMotor[0], 0)
	GPIO.pwmWrite(RightMotor[1], 1)

@webiopi.macro
def leftTurn():
	GPIO.pwmWrite(LeftMotor[0], 0.5)
	GPIO.pwmWrite(LeftMotor[1], 0)
	GPIO.pwmWrite(RightMotor[0], 1)
	GPIO.pwmWrite(RightMotor[1], 0)

@webiopi.macro
def leftRoll():
	GPIO.pwmWrite(LeftMotor[0], 0)
	GPIO.pwmWrite(LeftMotor[1], 1)
	GPIO.pwmWrite(RightMotor[0], 1)
	GPIO.pwmWrite(RightMotor[1], 0)

@webiopi.macro
def rightTurn():
	GPIO.pwmWrite(LeftMotor[0], 1)
	GPIO.pwmWrite(LeftMotor[1], 0)
	GPIO.pwmWrite(RightMotor[0], 0.5)
	GPIO.pwmWrite(RightMotor[1], 0)

@webiopi.macro
def rightRoll():
	GPIO.pwmWrite(LeftMotor[0], 1)
	GPIO.pwmWrite(LeftMotor[1], 0)
	GPIO.pwmWrite(RightMotor[0], 0)
	GPIO.pwmWrite(RightMotor[1], 1)
