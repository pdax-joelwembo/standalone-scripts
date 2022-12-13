import  jpype     
import  asposecells  
import requests
import json
import asyncio

jpype.startJVM() 
from asposecells.api import Workbook
workbook = Workbook("result2.xlsx")
workbook.save("file.json")
jpype.shutdownJVM()


def participants_data_migration(endpoint: any, data: any, file:any) -> None:
    for bank in data:
        r = requests.post(endpoint, json=bank)
        print(f"Status Code: {r.status_code}, Response: {r.json()}")


if __name__ == "__main__":
    endpoint = 'https://dev.api.sandbox.pdax.ph/ips-payments/destination-participant'
    file = open('file.json')
    data = json.load(file)
    participants_data_migration(endpoint , data, file)
  