# NOTE: If this fails to run, turn off the SPI and I2C interfaces.
# Turn them back on when this lab is complete.
# Alternatively, you can use the lesser abstracted RPi.GPIO interface
#   in the LightWater_RPi.GPIO.py file.
from gpiozero import LEDBarGraph
from pathlib import Path
import sys
from time import sleep
USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 
ADC = ADCDevice()
LED_PINS : list[int] = [17, 18, 27, 22, 23, 24, 25, 20, 13, 12]
LEDS = LEDBarGraph(*LED_PINS, active_high=False)

def setup():
    global LEDS
    for led in LEDS:  # make led(on) move from left to right
        led.off()
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
    

            
def loop():
    global ADC, LEDS
    while True:
        value = ADC.analogRead(0)   # read the ADC value of channel 0
        possible_levels = [0, 25.5, 51, 76.5, 102, 127.5, 153, 178.5, 204, 229.5]
        for i in range (0,len(possible_levels)):
            if value > possible_levels[i]:
                for led in LEDS:
                    led.off()
                for led in LEDS[:i]:
                    led.on()
        sleep(.01)
        
                
        voltage = value / 255.0 * 3.3
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} ')
        sleep(0.01)
                    
def destroy():
    global LEDS, ADC
    for led in LEDS:  # make led(on) move from left to right
        led.close()
    ADC.close()

if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()