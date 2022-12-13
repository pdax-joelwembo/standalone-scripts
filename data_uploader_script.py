import requests
import json
# Opening JSON file

endpoint = 'https://dev.api.sandbox.pdax.ph/ips-payments/destination-participant'
file = open('file.json')
data = json.load(file)

for bank in data:
    r = requests.post(endpoint, json=bank)
    print(f"Status Code: {r.status_code}, Response: {r.json()}")

file.close()    