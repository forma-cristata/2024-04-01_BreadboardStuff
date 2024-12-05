import RPi.GPIO as GPIO

class LaserCombo:
    laser_pin: int
    receiver_pin: int
    verbose: bool
    
    def __init__(self, laser_pin: int, receiver_pin: int, verbose: bool=True):
        self.laser_pin = laser_pin
        self.receiver_pin = receiver_pin
        self.verbose = verbose
        
        if verbose:
            print (f'Attempting to use pin {self.laser_pin} for the laser...')
        
        GPIO.setup(self.laser_pin, GPIO.OUT)
        GPIO.output(self.laser_pin, GPIO.LOW)
        
        if verbose:
            print (f'Attempting to use pin {self.receiver_pin} for the receiver...')
        
        GPIO.setup(self.receiver_pin, GPIO.IN)
        
        if verbose:
            print ('Setup complete.\n')


    def is_laser_aligned(self) -> bool:
        inputs = []
        for _ in range(0, 3):
            inputs.append(True if GPIO.input(self.receiver_pin) == 0 else False)
        
        inputs.sort()
        return inputs[1]
    
if __name__ == '__main__':    # Program entrance
    print ('This file has no executable.')