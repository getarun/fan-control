# coding=utf-8
import RPi.GPIO as GPIO
from config import Config

class RelayService():

    def __init__(self, relay_gpio_pins):
        self.pins = relay_gpio_pins
        self.state = {}
        GPIO.setmode(GPIO.BOARD)
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
        self.state[nr] = state

    def is_on(self, nr):
        return self.state[nr] == Config.RELAY_ON

    def is_off(self, nr):
        return self.state[nr] == Config.RELAY_OFF





