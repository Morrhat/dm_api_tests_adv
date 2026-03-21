"""
curl -X 'POST' \
  'http://185.185.143.231:5051/v1/account' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "login": "string",
  "email": "string",
  "password":  "string"
}'
"""
import pprint

"""
curl -X 'PUT' \
  'http://185.185.143.231:5051/v1/account/e4e4b4b8-78b5-4c97-9009-5ba232f1d2a2' \
  -H 'accept: text/plain'
"""

import requests

url = 'http://185.185.143.231:5051/v1/account'
headers = {
    'accept': '*/*',
    'Content-Type': 'application/json',
}
json = {
    "login": "Astarion_test_2",
    "email": "Astarion_test_2@mail.com",
    "password": "1234567890"
}

response = requests.post(url=url, json=json, headers=headers)

print(response.status_code)

url = 'http://185.185.143.231:5051/v1/account/6d907d92-86ca-4b52-a561-93b1541f4f3d'
headers = {
    'accept': 'text/plain'
}

response = requests.put(url=url, headers=headers)

print(response.status_code)
pprint.pprint(response.json())
response_json = response.json()
print(response_json['resource']['rating']['quantity'])
