import RPi.GPIO as GPIO
import time
from LaserCombo import LaserCombo

laserCombo: LaserCombo

def setup():
    global laserCombo
    GPIO.setmode(GPIO.BOARD)
    laserCombo = LaserCombo(37, 40)

def loop():
    global laserCombo
    while True:
        print(laserCombo.is_laser_aligned())
        time.sleep(0.5)

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()