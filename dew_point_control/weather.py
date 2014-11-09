# coding=utf-8
from config import Config
import time
import Adafruit_DHT
import numpy


class WeatherDataProvider():

    def __init__(self, dht22_pin):
        self.dht22_pin = dht22_pin
        self.last_update_time = 0
        self._temperature = -100
        self._humidity = -1

    def _get_temperature(self):
        self._update()
        return self.temperature

    def _get_humidity(self):
        self._update()
        return self.humidity

    def _get_dew_point(self):
        """According to http://en.wikipedia.org/wiki/Dew_point
        """
        self._update()
        B = 17.62
        C = 243.12  # unit °C
        return C * (B * self._temperature / (C + self._temperature) + numpy.log(self._humidity / 100.0)) / \
               (B * C / (C + self._temperature) - numpy.log(self._humidity / 100.0))


    def _update(self):
        current_time = time.time()
        if current_time - self.last_update_time > Config.DHT22_MIN_UPDATE_TIME:
            self._humidity, self._temperature = Adafruit_DHT.read_retry(Config.DHT22_MODEL, self.dht22_pin)
            self.last_update_time = current_time

    temperature = property(_get_temperature)
    humidity = property(_get_humidity)
    dew_point = property(_get_dew_point)
