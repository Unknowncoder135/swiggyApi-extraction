from sys import version
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import pandas as pd
import json
from bs4 import SoupStrainer


import sys
sys.stdout.reconfigure(encoding='utf-8')


headers = {
    'authority': 'www.swiggy.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    '__fetch_req__': 'true',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.swiggy.com/collections/11718?type=rcv2',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__SW=DImJ8h2scjrQI6ITHOPCq9htlGH2b0tC; _device_id=6fa523d1-bb65-48e0-af13-260de42fa7a3; fontsLoaded=1; userLocation=^{^%^22address^%^22:^%^22Mumbai^%^2C^%^20Maharashtra^%^2C^%^20India^%^22^%^2C^%^22area^%^22:^%^22^%^22^%^2C^%^22deliveryLocation^%^22:^%^22Mumbai^%^22^%^2C^%^22lat^%^22:19.0759837^%^2C^%^22lng^%^22:72.8776559^}; _guest_tid=ed51c84e-6440-4126-b51b-7bc85084607a; _sid=v7beea63-cfc5-47c1-ac74-1528d980793c',
}

params = (
    ('lat', '19.0759837'),
    ('lng', '72.8776559'),
    ('collection', '11718'),
    ('offset', '0'),
    ('pageType', 'COLLECTION'),
    ('type', 'rcv2'),
    ('page_type', 'DESKTOP_COLLECTION_LISTING'),
)

response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', headers=headers, params=params)

response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5?lat=19.0759837&lng=72.8776559&collection=11718&offset=0&pageType=COLLECTION&type=rcv2&page_type=DESKTOP_COLLECTION_LISTING', headers=headers)
response = response.text
# print(response)
data = json.loads(response)
page__no= data['data']['pages']
# print(page__no)
main_list = []
main = json.loads(response)
mmdata = main['data']['cards']

for x in range(len(mmdata)):
    try:
        name = mmdata[x]['data']['data']['name']
        # print(name)
    except:
        name = "null"
    try:
        area = mmdata[x]['data']['data']['area']
        
    except:
        area =  "null"
    try:
        deliveryTime = mmdata[x]['data']['data']['deliveryTime']
        
    except:
        deliveryTime = "null"
    try:
        restaurant = mmdata[x]['data']['data']['slugs']['restaurant']
    except:
        restaurant = "null"
    try:
        city = mmdata[x]['data']['data']['slugs']['city']
        
    except:
        city = "null"
    try:
        locality = mmdata[x]['data']['data']['locality']
        # print(locality)
    except:
        locality = "null"
    try:
        slaString = mmdata[x]['data']['data']['slaString']
        # print(locality)
    except:
        slaString = "null"
    if name == "null":
        continue
    else:
         main_dir = {
            "restaurant_name":restaurant,
            "restaurant_city": city,
            "restaurant_locality":locality,
            "sub-name":name,
            "restaurant_deliveryTime":deliveryTime,
            "restaurant_selString":slaString
        }
        

    main_list.append(main_dir)
print(main_list)


main_csv = pd.DataFrame(main_list)
main_csv.to_csv('main_data.csv',index=False)