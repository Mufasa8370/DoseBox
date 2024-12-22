# We imports the GPIO module
import RPi.GPIO as GPIO
# We import the command sleep from time
from time import sleep

# Stops all warnings from appearing
GPIO.setwarnings(False)

print("Setting up GPIO mode to BOARD...")
# We name all the pins on BOARD mode
GPIO.setmode(GPIO.BOARD)

print("Configuring pin 16 as an output...")
# Set an output for the PWM Signal
GPIO.setup(16, GPIO.OUT)

print("Initializing PWM on pin 16 at 50Hz...")
# Set up the PWM on pin #16 at 50Hz
pwm = GPIO.PWM(16, 50)

print("Starting PWM with 0 duty cycle...")
pwm.start(0) # Start the servo with 0 duty cycle ( at 0 deg position )

print("Moving servo to -90 degrees...")
pwm.ChangeDutyCycle(5) # Tells the servo to turn to the left ( -90 deg position )
sleep(0.5) # Tells the servo to Delay for 5sec

print("Moving servo to neutral position (0 degrees)...")
pwm.ChangeDutyCycle(7.5) # Tells the servo to turn to the neutral position ( at 0 deg position )
sleep(0.5) # Tells the servo to Delay for 5sec

print("Moving servo to +90 degrees...")
pwm.ChangeDutyCycle(10) # Tells the servo to turn to the right ( +90 deg position )
sleep(0.5) # Tells the servo to Delay for 5sec

print("Stopping PWM...")
pwm.stop(0) # Stop the servo with 0 duty cycle ( at 0 deg position )

print("Cleaning up GPIO...")
GPIO.cleanup() # Clean up all the ports we've used.

print("Program completed.")
