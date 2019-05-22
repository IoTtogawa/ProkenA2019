import webiopi
GPIO = webipi.GPIO

leftMotorDrivePWM1 = 
rightMotorDrivePWM1 = 

def setup():
	webiopi.debug("setup")

	GPIO.setFunction(leftMotorDrivePWM1, GPIO.PWM)
	GPIO.setfunction(rightMotorDrivePWM1, GPIO.PMM)

@webiopi.macro

def forward():
	webipi.debug("forward");

	GPIO.pwmWrite(leftMotorDrivePWM1, GPIO.LOW)
        GPIO.pwmWrite(rightMotorDrivePWM1, GPIO.LOW)

@webiopi.macro

def reverse():
        webipi.debug("reverse");

        GPIO.pwmWrite(leftMotorDrivePWM1, GPIO.LOW)
        GPIO.pwmWrite(rightMotorDrivePWM1, GPIO.LOW)

@webiopi.macro


