from gpiozero import LED as LEDClass, Button

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin

def loop():
    global LED, BUTTON
    while True:
        if BUTTON.is_pressed:  # if button is pressed
            LED.on()  # turn on led
            print ("led turned on >>>")  # print information on terminal
        else:  # if button is released
            LED.off()  # turn off led 
            print ("led turned off <<<")    

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

