import RPi.GPIO as GPIO
import Adafruit_DHT

class Config():

    FAN_RELAY_NUMBERS = (2, 3)
    AIR_DRYER_NUMBER = 1
    RELAY_GPIO_PINS = (18, 15, 13, 11)
    RELAY_OFF = GPIO.HIGH
    RELAY_ON = GPIO.LOW

    DHT22_MODEL = Adafruit_DHT.DHT22
    DHT22_PIN_INSIDE = 18
    DHT22_PIN_OUTSIDE = 23
    DHT22_MIN_UPDATE_TIME = 3.0

    DATA_LOG = '/var/log/fan-control/data.csv'
