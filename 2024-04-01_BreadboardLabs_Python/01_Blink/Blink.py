from gpiozero import LED as LEDClass # Alias
import time

LED = LEDClass(17)  # define led
LED_2 = LEDClass(18)

def loop():
    global LED
    while True:
        LED.on() 
        LED_2.off()
        print ("led turned on , led_2 turned off>>>") # print information on terminal
        time.sleep(1)
        LED.off()
        LED_2.on()
        print ("led turned off , led_2 turned on<<<")
        time.sleep(1)
        
def destroy():
    global LED
    # Release resources
    LED.close()
    LED_2.close()#changed

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using pin {LED.pin}")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
