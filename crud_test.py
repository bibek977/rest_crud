import requests
import json

url = "http://127.0.0.1:8000/crud_api/crud_class/"

# def get_data(id=None):
#     data = {}

#     if id is not None:
#         data = {'id':id}

#     json_data = json.dumps(data)
#     r = requests.get(url=url, data=json_data)
#     print(r.json())

# get_data(1)
# get_data()

# def post_data():
#     data = {
#         "Title": "The Avengers",
#         "Country": "USA",
#         "Language": "English",
#         "Director": "Joss Whedon",
#         "Writer": "Joss Whedon",
#         "Actors": "Robert Downey Jr",
#         "Actress": "Scarlet Johanson",
#         "Genre": "Action",
#         "Type": "movie",
#         "Year": 2012,
#         "imdbRating": 8,
#         "Runtime": 143
#     }

#     json_data = json.dumps(data)
#     r= requests.post(url=url, data=json_data)
#     print(r.json())

# post_data()


def update_data(id):
    data = {
        'id':id,
        "Title": "thor 4",
        "Country": "USA",
        "Language": "English",

        "Actors": "Chris Hemsworth",
        "Actress": "Scarlet Johanson",

        "Year": 2012,
        "imdbRating": 8,
        "Runtime": 143
    }

    json_data = json.dumps(data)
    r= requests.put(url=url, data=json_data)
    print(r.json())

update_data(1)

# def delete_data(id):
#     data = {
#         'id' : id
#     }

#     json_data = json.dumps(data)
#     r = requests.delete(url=url , data=json_data)
#     print(r.json)

# delete_data(3)