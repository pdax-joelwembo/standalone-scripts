from urllib.request import HTTPBasicAuthHandler
import requests
import json
import numpy as np
import pandas as pd

# Oath and Authentification
# Services url
excel_file = "./data/channels_bank_list_updated_2.xlsx"
api = 'https://api-dev.trade.pdax.ph/limits/channel'
channels_endpoint = open('data/channels.json') # We used this just speed up getting channel list
channels = json.load(channels_endpoint)['data']

# example adding parameters

df = pd.read_excel(excel_file)

# Looping tru channels json data ( ) : Replace the json file with actual api endpoint with oath
# https://api-dev.trade.pdax.ph/limits/channel

for channel in channels:
    channel_id = channel['id']
    channel_isHidden = channel['isHidden']
    channel_value = channel['value']

    if (channel_isHidden == True):
        # Iterate the excel file and get transferType and bankcode
        bankName = df['name'].where(df['value'] == channel_value  )
        transferType = df['transferType'].where(df['value'] == channel_value  )
        bankCode = df['bankCode'].where(df['value'] == channel_value )
        # get specific row after search
        bankName = (bankName.dropna()).values[0]
        transferType = (transferType.dropna()).values[0]
        bankCode = (bankCode.dropna()).values[0]
        print(f'Updating Bank:  {bankName} , Bank Code: {bankCode}, transferType: {transferType}' )

        # Params, data to be sent for patch endpoint : update
        params = dict (
        id = channel_id,
        transferType = transferType,
        bankCode = bankCode )

        r = requests.patch(api, params)
        print(f"Status Code: {r.status_code}, Response: {r.json()}")

    else:
        print('do nothing')    
