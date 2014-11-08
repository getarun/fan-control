# coding=utf-8
import RPi.GPIO as GPIO


class RelayService():

    OFF = GPIO.HIGH
    ON = GPIO.LOW

    def __init__(self, relay_gpio_pins=(18, 15, 13, 11)):
        self.pins = relay_gpio_pins
        GPIO.setmode(GPIO.BOARD)
        self.setup_pins()

    def setup_pins(self):
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, self.OFF)

    def switchOn(self, nr):
        self.switch(nr, self.ON)

    def switchOff(self, nr):
        self.switch(nr, self.OFF)

    def switch(self, nr, state):
        GPIO.output(self.pins[nr], state)




