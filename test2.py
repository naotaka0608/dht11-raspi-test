#!/usr/bin/env python
#coding:utf-8

import requests
import json

url = 'http://127.0.0.1:3000/sensor/'

data = { 'date': '2023-04-10T00:00:00.000+00:00', 'humidity': 32.0, 'temperature': 60.0 }

data_encode = json.dumps(data)
#response = requests.post(url, data=data_encode)
response = requests.post(url, data)

print(response)