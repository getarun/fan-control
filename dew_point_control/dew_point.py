# coding=utf-8
import Adafruit_DHT
import numpy
import Adafruit_CharLCD as LCD

class DewPointControl():
    def __init__(self, dht22_pin_inside=18, dht22_pin_outside=23):
        self.dht22_pin_outside = dht22_pin_outside
        self.dht22_pin_inside = dht22_pin_inside
        self.lcd = LCD.Adafruit_CharLCDPlate()
        self.lcd.set_color(1.0, 0.0, 0.0)
        self.lcd.create_char(1, [14, 10, 14, 0, 0, 0, 0, 0])
        self.lcd.clear()

    def get_measurement(self, inside):
        pin = self.dht22_pin_inside if inside else self.dht22_pin_outside
        return Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)

    def get_dew_point(self, humidity, temperature):
        """According to http://en.wikipedia.org/wiki/Dew_point
        """
        B = 17.62
        C = 243.12  # unit °C
        return C * (B * temperature / (C + temperature) + numpy.log(humidity / 100.0)) / \
               (B * C / (C + temperature) - numpy.log(humidity / 100.0))

    def show_dew_point(self, inside=True):
        humidity, temperature = self.get_measurement(inside)

        dew_point = self.get_dew_point(humidity, temperature)

        message = "%.1f\x01C %.1f%%\nDP: %.1f\x01C" % (temperature, humidity, dew_point)
        print message
        self.show_message(message)

    def show_message(self, message):
        self.lcd.clear()
        self.lcd.message(message)


DewPointControl().show_dew_point()


