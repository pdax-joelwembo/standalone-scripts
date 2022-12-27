import pandas as pd
df_json = pd.read_json('data/channels_bank_list.json')
df_json.to_excel('data/channels_bank_list.xlsx')
