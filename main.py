#!/usr/bin/env python
#coding:utf-8

import requests
import json
import RPi.GPIO as GPIO
import dht11
import time
from datetime import datetime

url = 'http://192.168.2.116:3000/sensor/'


def ExecuteSensor():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

    module = dht11.DHT11(pin=18)

    date = 0
    humidity = 0
    temperature = 0

    while True:
        result = module.read()
        if result.is_valid():
            print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            print("??: " + str(result.temperature) + "?")
            print("??: " + str(result.humidity) + "%")
            
            date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            #date = '2023-04-10T00:00:00.000+00:00'
            humidity = result.humidity
            temperature = result.temperature
            break
        time.sleep(1)

    data = { 'date': date, 'humidity': humidity, 'temperature': temperature }

    response = requests.post(url, data)

    print(response)

def main():
    ExecuteSensor()


if __name__ == "__main__":
    main()
