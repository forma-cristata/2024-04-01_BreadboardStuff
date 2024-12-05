from gpiozero import LED as LEDClass, Button
from signal import pause
from time import sleep

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin
is_strobing = True

def changeLedState():
    global is_strobing
    is_strobing = not is_strobing
   
def loop():
    global is_strobing
    while(True):
        if is_strobing:
            LED.on()
            sleep(.1)
            LED.off()
            sleep(.1)
            

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        # If the button gets pressed, call the function
        # This is an event
        
        BUTTON.when_pressed = changeLedState
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

