import RPi.GPIO as GPIO
import Adafruit_DHT

class Config():

    FAN_RELAY_NUMBERS = (0, 1)
    AIR_DRYER_NUMBER = 2
    RELAY_GPIO_PINS = (11, 13, 15, 18)
    RELAY_OFF = GPIO.HIGH
    RELAY_ON = GPIO.LOW

    DHT22_MODEL = Adafruit_DHT.DHT22
    DHT22_PIN_INSIDE = 18
    DHT22_PIN_OUTSIDE = 23
    DHT22_MIN_UPDATE_TIME = 3.0

    DATA_LOG = '/var/log/fan-control/data.csv'
