# coding=utf-8
from config import Config
from relay import RelayService
from display import DisplayProvider
from weather import WeatherDataProvider


class DewPointControl():
    def __init__(self):
        self.inside = WeatherDataProvider(Config.DHT22_PIN_INSIDE)
        self.outside = WeatherDataProvider(Config.DHT22_PIN_OUTSIDE)
        self.lcd = DisplayProvider()
        self.relays = RelayService(Config.RELAY_GPIO_PINS)

    def show_dew_point(self, inside=True):
        message = "%.1f\x01C %.1f%%\nDP: %.1f\x01C" % (self.inside.temperature, self.inside.humidity, self.inside.dew_point)
        print message
        self.show_message(message)

    def show_message(self, message):
        self.lcd.clear()
        self.lcd.show(message)


DewPointControl().show_dew_point()


