import requests
import json

api = "https://api-dev.trade.pdax.ph/limits/channel"
headers = {
     "Authorization": "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..KXYuSSiO0mxCyKXAsAKjow.WNV5lQVSWYvWeBFm52IhdoEsDolvinBGJQE5x0YoIY_kZGMiymDXvX9YAolgXceGVdnPHoGtsvY5-DEHVQzYkB3yFsdR3zJu50YVWPOJPgJYA3ugp0LDCam_OIZZTspQlI2HE_07L-zKfhU4mozKJwPd-wiNB10p9FS5x9QNsfQSMRnhyApsqXqnllx79SsjC_zb2CsskWIWzaqTwFX7YgVVxkELg2HQt579RFbnHQ2GUXYP4g2l8JJ3TWvqI2-BeUeMBi6njIxpmLYQ3NJamK00yDpLNb-rBNj4JTrJq9WWwiEX537HxgFAiu06s4g7dgqd6KM0RFC4O22G0M3RU5cR6iBhbUNh0s7B7H4g7DC7gEar2NO5oSdpQtvfyKxI.FFyqH5qXQTAyPcMmNMsSHQ",
}
# response = requests.get(api, headers=headers)
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())

response = requests.get(api, headers=headers)
response_channels = response.json()['data'] 
print(response_channels)
