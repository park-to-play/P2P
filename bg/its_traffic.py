import requests
import json
import pandas as pd
import os
import time

its_traffic_save_folder = './its_traffic'
os.makedirs(its_traffic_save_folder, exist_ok=True)

# its 교통 소통 정보보
its_api_key = '44b2556c865a470180ca92814d20cbf6'
traffic_params = {
    'apiKey' : its_api_key,
    'type' : 'all',
    'minX' : 126.734086,
    'maxX' : 127.269311,
    'minY' : 37.413294,
    'maxY' : 37.715133,
    'getType' : 'json'
    
}
its_traffic_api_url = 'https://openapi.its.go.kr:9443/trafficInfo?'

def its_traffic_data(its_traffic_api_url, traffic_params):
    print('start its_traffic.py')
    its_traffic_res = requests.get(its_traffic_api_url, params=traffic_params)
    its_traffic_res.status_code

    its_traffic_data = its_traffic_res.json()
    print(its_traffic_data)
    its_traffic_items = its_traffic_data["body"]["items"]
    its_traffic_df = pd.DataFrame(its_traffic_items)

    its_traffic_file_name = f'its_traffic_data_{time.strftime("%Y-%m-%d_%H%M%S")}.csv'
    save_path = os.path.join(its_traffic_save_folder, its_traffic_file_name)
    its_traffic_df.to_csv(save_path, index=False, encoding='utf-8-sig')
    print(f"save complite : {its_traffic_file_name}")



start_time = time.time()
its_traffic_data(its_traffic_api_url, traffic_params)
while True:
    chek_time = time.time()
    if int(chek_time - start_time) > 1200:
        its_traffic_data(its_traffic_api_url, traffic_params)
        start_time = chek_time # 시간을 다시 초기화
