import requests
import json

# url = "http://127.0.0.1:8000/api/"
# r=requests.get(url=url)
# data = r.json()
# print(data)



# url = "http://127.0.0.1:8000/intern_api/create_intern/"

# data = {
#     # 'id' : 9,
#     'name' : 'Bibek Bhattarai',
#     'phone' : 9810258171,
#     'location' : "Balkumari",
#     'program' : 'Django'
# }



url = "http://127.0.0.1:8000/api/create_home/"

data = {
    "title": "300",
    "country": "USA",
    "imdb": 7.7,
    "director": "Zack Snyder",
    "runtime": 117
}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))

r = requests.post(url=url, data=json_data)
print(r.json())
