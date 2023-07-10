#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse
import requests
from env_sensors import display_sensors_data

main_api = "http://172.16.96.32:5000/api/"
url = main_api + "env_sensors"
print("URL: " + (url))

json_data = requests.get(url).json()
print('Voici les données recueillies par les capteurs physiques')
display_sensors_data(json_data)