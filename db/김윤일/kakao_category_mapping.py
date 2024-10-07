import requests
import json
import pandas as pd
import time
from geopy.distance import geodesic

parking_df = pd.read_csv('parking_data_20241001_1120.csv')

def kakao_category_mapping(df): # 위경도로 입력 변경시 데이터프레임에 바로 적용가능
    parking_selected_columns_df = df[['주차장 이름', '위도', '경도']].copy()
    
    kakao_rest_api_key = ''  # kakao api key 입력

    category_headers = {
        'Authorization': f'KakaoAK {kakao_rest_api_key}'
    } 
    kakao_category_rest_api_url = 'https://dapi.kakao.com/v2/local/search/category.json?'
    
    saved_data = []
    category_codes = ['MT1', 'CS2', 'PS3', 'SC4', 'AC5', 'PK6', 'OL7', 'SW8', 'BK9', 'CT1', 'AG2', 'PO3', 'AT4', 'AD5', 'FD6', 'CE7', 'HP8', 'PM9']

    for index, row in parking_selected_columns_df.iterrows():
        print(f"Processing row at index: {index}")
        x = row['위도']
        y = row['경도']
        for category_code in category_codes:
            category_params = {
            'category_group_code' : category_code,
            'y' : y,
            'x' : x,
            'radius' : 1000,
            'sort' : 'distance'
            }
            
            res = requests.get(kakao_category_rest_api_url, headers=category_headers, params=category_params)
            
            if res.status_code == 200:
                search_data = res.json()
                documents = search_data.get('documents',[])

                for item in documents:
                    saved_data.append({
                        '주차장 이름' : row['주차장 이름'],
                        'search_point' : (x, y),
                        'category_group_code' : category_code,
                        'address_name' : item.get('address_name', ''),
                        'category_group_code' : item.get('category_group_code', ''),
                        'category_group_name' : item.get('category_group_name', ''),
                        'category_name' : item.get('category_name', ''),
                        'distance' : item.get('distance', ''),
                        'id' : item.get('id', ''),
                        'phone' : item.get('phone', ''),
                        'place_name' : item.get('place_name', ''),
                        'place_url' : item.get('place_url', ''),
                        'road_address_name' : item.get('road_address_name', ''),
                        'x' : item.get('x', ''),
                        'y' : item.get('y', '')
                    })
            time.sleep(0.5)
        # break        
    df = pd.DataFrame(saved_data)
    df.to_csv('./data/category_output_data_241001.csv', index=False, encoding='utf-8-sig')
    print('saved complite.  category_output_data_241001.csv')
    
    
kakao_category_mapping(parking_df)