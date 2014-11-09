#!/usr/bin/env python

#from ez_setup import use_setuptools
#use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'dew_point_control',
      version 			= '0.0.1',
      author			= 'Sebastian Herold',
      description		= 'Software two control fans dependent on temperature and humidity.',
      license			= 'GPL',
      url				= 'https://github.com/heroldus/dew_point_control/',
      dependency_links	= ['https://github.com/adafruit/Adafruit_Python_CharLCD/tarball/master#egg=Adafruit_CharLCD-1.0.0'],
      install_requires	= ['Adafruit_CharLCD>=1.0.0'],
      packages 			= find_packages())
