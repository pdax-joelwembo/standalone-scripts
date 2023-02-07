import json
import pandas
import  jpype     
import  asposecells   
import requests

# Script to generate json from the excel edited channels bank list
# jpype.startJVM() 
# from asposecells.api import Workbook
# workbook = Workbook("data/channels_bank_list_updated_2.xlsx")
# workbook.save("data/channels_bank_list_updated_3.json")
# jpype.shutdownJVM()
# Script to generate json from the excel edited channels bank list
# output : data/channels_bank_list_updated_3.json
api = 'https://api-dev.trade.pdax.ph/limits/channel'
headers = {
     "Authorization": "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..KXYuSSiO0mxCyKXAsAKjow.WNV5lQVSWYvWeBFm52IhdoEsDolvinBGJQE5x0YoIY_kZGMiymDXvX9YAolgXceGVdnPHoGtsvY5-DEHVQzYkB3yFsdR3zJu50YVWPOJPgJYA3ugp0LDCam_OIZZTspQlI2HE_07L-zKfhU4mozKJwPd-wiNB10p9FS5x9QNsfQSMRnhyApsqXqnllx79SsjC_zb2CsskWIWzaqTwFX7YgVVxkELg2HQt579RFbnHQ2GUXYP4g2l8JJ3TWvqI2-BeUeMBi6njIxpmLYQ3NJamK00yDpLNb-rBNj4JTrJq9WWwiEX537HxgFAiu06s4g7dgqd6KM0RFC4O22G0M3RU5cR6iBhbUNh0s7B7H4g7DC7gEar2NO5oSdpQtvfyKxI.FFyqH5qXQTAyPcMmNMsSHQ",
}
# get all channels from the api endpoint
response = requests.get(api, headers=headers)
response_channels = response.json()['data'] 
# print(response_channels)
# # Processed channels list from the excel file
channels_list = open('data/channels_bank_list_updated_2.json')
channels = json.load(channels_list)


# # iterating thru the channels json list from api endoint                  
for element in response_channels:
    element_id = element['id']
    element_value = element['value']
    element_transferType = element['transferType']
    element_bankCode = element['bankCode']
    newIsHidden = True
    
    # iterating thru the channels from the excel file
    for channel in channels:
        channel_value = channel['value']
        channel_status = channel['status']
        channel_bankCode = channel['bankCode']
        channel_transferType = channel['transferType']
        channel_isHidden = channel['isHidden']
        newIsHidden = channel_isHidden
   
        print(f"Channel: {channel_value}, is : {channel_status}")
            # Params, data to be sent for patch endpoint : update
            # Reponse channel refer to the json load of api endpoint
            
        if len(channel_bankCode) > 0:
            newBankCode = channel_bankCode       
        if len(channel_transferType) > 0:
            newTransferType = channel_transferType        
        if channel_isHidden == "hidden":
            newIsHidden = True  
            
        request_body = {
            "id": element_id,
            "bankCode": element_bankCode,
            "transferType": element_transferType,
            "isHidden": newIsHidden
        }
        request_body = json.dumps(request_body)

            
    # Comparaing the value name of the channels on excel and api
        if element_value == channel_value:    
            # send patch request
            r = requests.patch(api, request_body, headers=headers)
            print(f"Status Code: {r.status_code}, Response: {r.json()}")
