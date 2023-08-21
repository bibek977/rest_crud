from django.test import TestCase

import requests
import json

url = "http://127.0.0.1:8000/crud_api/crud_class/"

def post_data():
    data = {
        "Title": "The Avengers",
        "Country": "USA",
        "Language": "English",
        "Director": "Joss Whedon",
        "Writer": "Joss Whedon",
        "Actors": "Robert Downey Jr",
        "Actress": "Scarlet Johanson",
        "Genre": "Action",
        "Type": "movie",
        "Year": 2012,
        "imdbRating": 8,
        "Runtime": 143
    }

    json_data = json.dumps(data)
    r= requests.post(url=url, data=json_data)
    print(r.json())

post_data()