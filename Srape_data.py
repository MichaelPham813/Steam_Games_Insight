from urllib import request
from pprint import pprint
import json
import pandas as pd
MAX_PAGES = 79
data_lib = []
for number in range(MAX_PAGES):
    URL = f'https://steamspy.com/api.php?request=all&page={number}'
    access_page = request.urlopen(URL)

    data = json.load(access_page)


    for key,value in data.items():
        data_template = {
            'appid': value['appid']
            ,'name': value['name']
            ,'developer': value['developer']
            ,'publisher': value['publisher']
            ,'positive': value['positive']
            ,'negative': value['negative']
            ,'owners': value['owners']
            ,'initial_price': value['initialprice']
            ,'discount': value['discount']
            ,'price': value['price']
        }
        data_lib.append(data_template)
    

    df = pd.DataFrame(data_lib)
    column_name = [
                    'App ID', 'Game Name', 'Developer', 'Publisher','Positive'
                   ,'Negative','Range of Owners','Initial Price','Discount','Price'
                   ]
    df.to_csv('steam_game.csv',sep=',',header=column_name,index=False)

    


    



