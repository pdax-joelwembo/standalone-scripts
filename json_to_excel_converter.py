import pandas as pd
from pandas.io.json import json_normalize #package for flattening json in pandas df

df_json = pd.read_json('data/channels_bank_list.json')
data = pd.DataFrame(df_json)
data = json_normalize(data['data'])
data.drop(['outlets', 'notes', 'coverage', 'turnAroundTime', 'imageSmall', \
'imageMedium', 'limitMin', 'limitMax','feeAmount' , 'pdaxFeeAmount', \
'feePercentage' , 'pdaxFeePercentage' , 'feeStructure' , 'pdaxFeeStructure' , \
'feeMode' ,  'pdaxFeeMode', 'banks', 'paymentMode',  'isDisabled', 'isUnavailable' , 'featureRank' , 'platform','createdAt', 'updatedAt'], inplace=True, axis=1)

# Add extra colum

data.insert(8 , 'instapay bank', '', True)
data.insert(9 , 'status', '', True)
data.insert(10 , 'transferType', '', True)
data.insert(11 , 'bankCode', '', True)
data.to_excel('data/channels_bank_list.xlsx')


