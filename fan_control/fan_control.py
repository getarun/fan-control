# coding=utf-8
from config import Config
from relay import RelayService
from display import DisplayProvider
from weather import WeatherDataProvider


class FanControl():
    def __init__(self):
        self.inside = WeatherDataProvider(Config.DHT22_PIN_INSIDE)
        self.outside = WeatherDataProvider(Config.DHT22_PIN_OUTSIDE)
        self.lcd = DisplayProvider()
        self.relays = RelayService(Config.RELAY_GPIO_PINS)

    def show_dew_point(self):
        message = "%.1f°C %.1f%%\nDP: %.1f°C" % (self.inside.temperature, self.inside.humidity, self.inside.dew_point)
        print message
        self.show_message(message)

    def switch_on_fans(self):
        for fan_nr in Config.FAN_RELAY_NUMBERS:
            self.relays.switch_on(fan_nr)

    def switch_off_fans(self):
        for fan_nr in Config.FAN_RELAY_NUMBERS:
            self.relays.switch_off(fan_nr)

    def switch_on_air_dryer(self):
        self.relays.switch_on(Config.AIR_DRYER_NUMBER)

    def switch_off_air_dryer(self):
        self.relays.switch_off(Config.AIR_DRYER_NUMBER)

    def show_message(self, message):
        self.lcd.clear()
        self.lcd.show(message)

    def update(self):
        self.show_dew_point()

if __name__ == "__main__":
    FanControl().update()


