import requests
import json

url = "http://127.0.0.1:8000/function_api/"

def get_data(id=None):
    data = {}

    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=url, headers=headers ,data=json_data)
    print(r.json())

# get_data(1)
# get_data()

def post_data():
    data = {
        'name':"Bibek Bhattarai",
        'phone' : 9810258171,
        'location' : "balkumari",
        'program' : 'Django'
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.post(url=url,headers=headers,data=json_data)
    print(r.json())

# post_data()

def update_data(id):
    data = {
        'id' : id,
        'name':"Bibek ",
        'location' : "piluwa",
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.put(url=url,headers=headers,data=json_data)
    print(r.json())

update_data(5)


def delete_data(id):
    data = {
        'id' : id,
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.delete(url=url,headers=headers,data=json_data)
    print(r.json())

delete_data(8)