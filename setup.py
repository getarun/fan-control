#!/usr/bin/env python

#from ez_setup import use_setuptools
#use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'fan_control',
      version 			= '0.0.1',
      author			= 'Sebastian Herold',
      description		= 'Software two control fans dependent on temperature and humidity.',
      license			= 'GPL',
      url				= 'https://github.com/heroldus/dew_point_control/',
      dependency_links	= ['https://github.com/adafruit/Adafruit_Python_CharLCD/tarball/master#egg=Adafruit_CharLCD-1.0.0',
                             'https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tarball/master#egg=Adafruit_DHT-1.0.0',
                             'https://github.com/martinrusev/python-daemon/tarball/master#egg=python_daemon-0.1.0'],
      install_requires	= ['Adafruit_CharLCD>=1.0.0', 'Adafruit_DHT>=1.0.0', 'python_daemon>=0.1.0'],
      packages 			= find_packages(),
      data_files        = [('/etc/init.d', ['fan-control']),
                           ('/var/www', ['www/index.html', 'www/dygraph-combined.js'])])

