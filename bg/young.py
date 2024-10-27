import requests
import json
import pandas as pd
import os
import time


class getITS():
    
    def its_traffic_data():
        its_api_key = '123123123123'
        its_traffic_api_url = 'https://openapi.its.go.kr:9443/trafficInfo?'
        traffic_params = {
            'apiKey' : its_api_key,
            'type' : 'all',
            'minX' : 126.734086,
            'maxX' : 127.269311,
            'minY' : 37.413294,
            'maxY' : 37.715133,
            'getType' : 'json'
            
        }
        its_traffic_res = requests.get(its_traffic_api_url, params=traffic_params)
        its_traffic_res.status_code

        its_traffic_data = its_traffic_res.json()
        its_traffic_items = its_traffic_data["body"]["items"]
        its_traffic_df = pd.DataFrame(its_traffic_items)
        return its_traffic_df