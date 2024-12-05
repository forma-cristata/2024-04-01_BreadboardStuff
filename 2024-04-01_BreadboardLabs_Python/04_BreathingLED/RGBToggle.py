from gpiozero import PWMLED, Button
import time

LED = PWMLED(18)  # define PWMLED
BUTTON = Button(25)
THIS_BOOLEAN = False
def loop():
    global LED
    global THIS_BOOLEAN
    if THIS_BOOLEAN:
        while True:
            i : int = 0
            # range() only works with integers
            for i in range(0, 10): # make the led brighter
                # led.value only accepts floats
                LED.value = i / 10 # set DC (direct current) value as the duty cycle
                time.sleep(0.1)
                
            for i in range(10, 0, -1): # dim the led
                LED.value = i / 10 # set DC value as the duty cycle
                time.sleep(0.1)
def changeBool():
    global THIS_BOOLEAN
    THIS_BOOLEAN = not THIS_BOOLEAN

def destroy():
    global LED
    LED.close()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    print(f"Using pin {LED.pin}")
    try:
        BUTTON.when_pressed = changeBool
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
