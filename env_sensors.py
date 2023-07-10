#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    from sense_hat import SenseHat
    sense = SenseHat()
except ImportError:
    sense = None
from time import sleep

def get_sensors_data():
    """Récupère les données suivantes des capteurs :
       - pression
       - températures, fournies respectivement par le
         - capteur d'humidité
         - capteur de pression
       - degré d'humidité

    :return: dictionnaire de la forme suivante :
             { 'pressure': 995.82,
               'temperature': { 'from_humidity': 35.78, 'from_pressure': 38.72},
               'humidity': 30.56 }
    """
    if sense:
        # récupération effective des données fournies par les capteurs du Sense HAT
        pressure = sense.get_pressure()
        temp_from_humidity = sense.get_temperature_from_humidity()
        temp_from_pressure = sense.get_temperature_from_pressure()
        humidity = sense.get_humidity()
    else:
        # simulation de ces données
        pressure = 1013.25  # pression atmosphérique standard
        temp_from_humidity = 35
        temp_from_pressure = 36
        humidity = 30

    return \
        {
            'pressure': pressure,
            'temperature': {
                'from_humidity': temp_from_humidity,
                'from_pressure': temp_from_pressure
            },
            'humidity': humidity
        }

def display_sensors_data(data):
    """Affiche les données des capteurs, avec une seule décimale pour chaque grandeur.

    :param data: dictionnaire de la forme suivante :
                 { 'pressure': 995.82,
                   'temperature': { 'from_humidity': 35.78, 'from_pressure': 38.72},
                   'humidity': 30.56 }
    """
    print('''\
- pression : {:.1f}
- température du capteur d’humidité : {:.1f}
- température du capteur de pression : {:.1f}
- taux d'humidité : {:.1f}'''.format(
        data['pressure'],
        data['temperature']['from_humidity'],
        data['temperature']['from_pressure'],
        data['humidity']))

def get_sensors_data_list(nb_data = 60, frequency = 1):
    """Récupère une série de données des capteurs, obtenues à la fréquence indiquée.

    :param nb_data: nombre de données à récupérer
    :param frequency: fréquence d'obtention de ces données
    :return: liste de la série de données
    """
    period = 1 / frequency
    data_list = []
    for _ in range(nb_data):
        data_list.append(get_sensors_data())
        sleep(period)
    return data_list

def get_sensors_data_average(data_list):
    """Calcule et retourne la moyenne de la série data_list de données des capteurs.

    :param data_list: série de données
    :return: données moyennées
    """
    sum_pressure = sum_temp_from_humidity = sum_temp_from_pressure = sum_humidity = 0
    nb_data = len(data_list)
    for data in data_list:
        sum_pressure           += data['pressure']
        sum_temp_from_humidity += data['temperature']['from_humidity']
        sum_temp_from_pressure += data['temperature']['from_pressure']
        sum_humidity           += data['humidity']
    return \
        {
            'pressure': sum_pressure / nb_data,
            'temperature': {
                'from_humidity': sum_temp_from_humidity / nb_data,
                'from_pressure': sum_temp_from_pressure / nb_data
            },
            'humidity': sum_humidity / nb_data
        }

if __name__ == "__main__":
    print('Voici la moyenne des données recueillies par les capteurs physiques, '
          'chaque seconde sur une minute :')
    display_sensors_data(get_sensors_data_average(get_sensors_data_list()))