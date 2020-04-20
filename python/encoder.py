from RPi import GPIO
from time import sleep
import threading

class Encoder:
                
    def __init__(self,Navigator):
        self.navigator=Navigator
        self.clk = 17
        self.dt = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.clkLastState = GPIO.input(self.clk)
        encoder = threading.Thread(target=self.listen, args=())
        encoder.start()
        
    def listen(self):
        try:
            while True:
                clkState = GPIO.input(self.clk)
                if clkState != self.clkLastState:
                    dtState = GPIO.input(self.dt)
                    if dtState != clkState:
                        self.navigator.analyse_cmd("+")
                    else:
                        self.navigator.analyse_cmd("-")

                self.clkLastState = clkState
                sleep(0.01)
        finally:
                GPIO.cleanup()
