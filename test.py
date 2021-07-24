#!/usr/bin/env python
#coding:utf-8

from mongoengine import connect, Document, EmbeddedDocument, \
    StringField, DecimalField, IntField, DateTimeField, ListField, EmbeddedDocumentField
from datetime import datetime

import RPi.GPIO as GPIO
import dht11
import time

connect(db='test',
        username="admin",
        password="password",
        host='192.168.2.117',
        port=27017,
        authentication_mechanism='SCRAM-SHA-1',
        authentication_source='admin'
        )


class Sensor_dht11(Document):
    temperature = DecimalField(min_value=0.0, max_value=100.0, required=True)
    humidity = DecimalField(min_value=0.0, max_value=100.0, required=True)
    createOn = DateTimeField(default=datetime.utcnow())


class Sensor:

    def __init__(self):
        self.result = []

    def ExecuteSensor(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        module = dht11.DHT11(pin=18)

        while True:
            self.result = module.read()
            if self.result.is_valid():
                print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                print("気温: " + str(self.result.temperature) + "度")
                print("湿度: " + str(self.result.humidity) + "%")
                break
            time.sleep(1)

    def add_one(self):
       obj = Sensor_dht11(
           temperature = self.result.temperature,
           humidity =self.result.humidity,
       )
       obj.save()
       return obj

if __name__ == "__main__":
    test = Sensor()
    test.ExecuteSensor()
    test.add_one()