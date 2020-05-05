from RPi import GPIO
from time import sleep
import threading

class Encoder:
                
    def __init__(self,Machine):
        self.machine=Machine
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
                        self.machine.navigator.analyse_cmd("encoder","+")
                    else:
                        self.machine.navigator.analyse_cmd("encoder","-")

                self.clkLastState = clkState
                sleep(0.01)
        finally:
                GPIO.cleanup()
