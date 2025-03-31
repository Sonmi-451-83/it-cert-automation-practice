#!/usr/bin/env python3

import os
import requests


def process_data(url, dir):

    fruit = {}
    for item in os.listdir(dir):
        fruit.clear()
        filename = os.path.join(dir, item)
        with open(filename) as file:
            line = file.readlines()
            fruit["name"] = line[0].strip('\n')
            fruit["weight"] = int(line[1].strip('\n').replace(" lbs", ""))
            fruit["description"] = line[2].strip('\n')
            fruit["image_name"] = (item.strip('.txt')) + '.jpeg'
            print(fruit)

            response = requests.post(url, json=fruit)
            if response.ok:
              print("uploaded data")
            else:
              print(f"error: {response.status_code}")



if __name__ == '__main__':
    url = 'http://localhost/fruits/'
    user = os.getenv('USER')
    directory = '/home/{}/supplier-data/descriptions/'.format(user)
    process_data(url, directory)