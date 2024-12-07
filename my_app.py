import requests
import json


URL = "http://127.0.0.1:8000/"


# Retrieving Data
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)

    response = r.json()
    print(response)

# get_data(2)


# Creating/Inserting Data
def post_data():
    data = {
        'name': 'Sangam',
        'roll': 106,
        'city': 'Varanasi'
    }

    json_data = json.dumps(data)

    r = requests.post(url=URL, data=json_data)
    response = r.json()

    print(response)


# post_data()


# Updating Data
def update_data():
    data = {
        'id': 5,
        'name': 'Rohit',
        'city': 'Ranchi'
    }

    json_data = json.dumps(data)

    r = requests.put(url=URL, data=json_data)
    response = r.json()

    print(response)

# update_data()


# Deleting Data
def delete_data():
    data = {
        'id': 5,
    }

    json_data = json.dumps(data)

    r = requests.delete(url=URL, data=json_data)
    response = r.json()
    print(response)

delete_data()
