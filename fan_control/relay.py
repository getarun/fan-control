# coding=utf-8
import RPi.GPIO as GPIO
from config import Config

class RelayService():

    def __init__(self, relay_gpio_pins):
        self.pins = relay_gpio_pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.setup_pins()

    def setup_pins(self):
        for index in range(len(self.pins)):
            GPIO.setup(self.pins[index], GPIO.OUT)
            self.switch_off(index)

    def switch_on(self, nr):
        self.switch(nr, Config.RELAY_ON)

    def switch_off(self, nr):
        self.switch(nr, Config.RELAY_OFF)

    def switch(self, nr, state):
        GPIO.output(self.pins[nr], state)

    def is_on(self, nr):
        GPIO.setup(self.pins[nr], GPIO.IN)
        try:
            return GPIO.input(self.pins[nr]) == Config.RELAY_ON
        finally:
            GPIO.setup(self.pins[nr], GPIO.OUT)

    def is_off(self, nr):
        return not self.is_on(nr)





