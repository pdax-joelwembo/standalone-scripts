from urllib.request import HTTPBasicAuthHandler
import requests
import json
import numpy as np
import pandas as pd

# Oath and Authentification
headers = {
     "Authorization": "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..KXYuSSiO0mxCyKXAsAKjow.WNV5lQVSWYvWeBFm52IhdoEsDolvinBGJQE5x0YoIY_kZGMiymDXvX9YAolgXceGVdnPHoGtsvY5-DEHVQzYkB3yFsdR3zJu50YVWPOJPgJYA3ugp0LDCam_OIZZTspQlI2HE_07L-zKfhU4mozKJwPd-wiNB10p9FS5x9QNsfQSMRnhyApsqXqnllx79SsjC_zb2CsskWIWzaqTwFX7YgVVxkELg2HQt579RFbnHQ2GUXYP4g2l8JJ3TWvqI2-BeUeMBi6njIxpmLYQ3NJamK00yDpLNb-rBNj4JTrJq9WWwiEX537HxgFAiu06s4g7dgqd6KM0RFC4O22G0M3RU5cR6iBhbUNh0s7B7H4g7DC7gEar2NO5oSdpQtvfyKxI.FFyqH5qXQTAyPcMmNMsSHQ",
}
# Services url
excel_file = "./data/channels_bank_list_updated_2.xlsx"
api = 'https://api-dev.trade.pdax.ph/limits/channel'

response = requests.get(api, headers=headers)
channels = response.json()['data'] 


print(channels)

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

        r = requests.patch(api, params, headers=headers)
        print(f"Status Code: {r.status_code}, Response: {r.json()}")

    else:
        print('id not correect or doesnt exist')    
