
""" 
Author : Joel Otepa Wembo
Date : 12/12/2022
Program to Convert Bank List to JSON File for destination_partners 
"""
import pandas
import json

# Read excel sheet document from .xlsx file extension
excel_data_df = pandas.read_excel('data/result2.xls', sheet_name='sheet1')
# Convert excel to string and define orientation of document in this case from up to down
thisisjson = excel_data_df.to_json(orient='records')
# Print out the result
print('Excel Sheet to JSON:\n', thisisjson)
# Make the string into a list to be able to input in to a JSON-file
thisisjson_dict = json.loads(thisisjson)
with open('data/data3.json', 'w') as json_file:
    json.dump(thisisjson_dict, json_file)