#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from env_sensors import get_sensors_data

app = Flask(__name__)

@app.route('/')
def main():
    data = get_sensors_data()
    data_html = '<ul>'
    data_html += '''\
    <li>pression : {:.1f}</li>
    <li>température du capteur d’humidité : {:.1f}</li>
    <li>température du capteur de pression : {:.1f}</li>
    <li>taux d'humidité : {:.1f}</li>'''.format(
        data['pressure'],
        data['temperature']['from_humidity'],
        data['temperature']['from_pressure'],
        data['humidity'])
    data_html += '</ul>'
    return data_html

@app.route('/api/env_sensors', methods=['GET'])
def get_env_sensors():
    return jsonify(get_sensors_data())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')