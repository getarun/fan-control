# coding=utf-8
from config import Config
from relay import RelayService
from display import DisplayProvider
from weather import WeatherDataProvider
import time


class FanControl():
    def __init__(self):
        self.inside = WeatherDataProvider(Config.DHT22_PIN_INSIDE)
        self.outside = WeatherDataProvider(Config.DHT22_PIN_OUTSIDE)
        self.lcd = DisplayProvider()
        self.relays = RelayService(Config.RELAY_GPIO_PINS)

    def show_dew_point(self):
        message = "%.1f° %.1f%% %.1f°\n%.1f° %.1f%% %.1f°" % \
                  (self.inside.temperature, self.inside.humidity, self.inside.dew_point,
                   self.outside.temperature, self.outside.humidity, self.outside.dew_point)
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

    def save_data(self):
        timestamp = int(time.time())
        time_string = time.strftime('%Y-%m-%d %H:%M:%S')
        with open(Config.DATA_LOG, 'a') as f:
            f.write('%s,%d,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%d,%d,%d,%d\n' %
                    (time_string, timestamp,
                     self.inside.temperature, self.inside.humidity, self.inside.dew_point,
                     self.outside.temperature, self.outside.humidity, self.outside.dew_point,
                     self.relays.is_on(0), self.relays.is_on(1), self.relays.is_on(2), self.relays.is_on(3)))

    def update(self):
        self.show_dew_point()
        self.save_data()

if __name__ == "__main__":
    FanControl().update()


