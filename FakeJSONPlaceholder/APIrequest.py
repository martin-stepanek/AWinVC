import requests
import json
import pprint

payload = {
    "token": "BjbwTrsK1uCxeZuLLh9anw",
    "data": {
      "name": "nameFirst",
      "email": "internetEmail",
      "phone": "phoneHome",
      "_repeat": 1
    }
}

r = requests.post("https://my-json-server.typicode.com/martin-stepanek/AWinVC", json = payload)

response = requests.get("https://my-json-server.typicode.com/martin-stepanek/AWinVC", json = payload)
pprint.pprint(response.text)

response = requests.get("https://my-json-server.typicode.com/martin-stepanek/AWinVC/db.json", json = payload)
pprint.pprint(response.text)

# Do something with fake data