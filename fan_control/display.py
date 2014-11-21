# coding=utf-8

import Adafruit_CharLCD as LCD


class DisplayProvider():

    def __init__(self):
        self.lcd = LCD.Adafruit_CharLCDPlate()
        self.lcd.set_color(1.0, 0.0, 0.0)
        self.lcd.create_char(1, [14, 10, 14, 0, 0, 0, 0, 0])
        self.lcd.create_char(2, [28, 20, 28, 3, 4, 4, 4, 3])
        self.lcd.clear()

    def show(self, msg):
        self.lcd.message(msg.replace('°', '\x02'))

    def clear(self):
        self.lcd.clear()

