import requests
import json
import time


def collect_and_save_traffic_data():

    url = "https://apis.openapi.sk.com/tmap/traffic"
    params = {
        "version": 1,
        "format": "json",
        "reqCoordType": "WGS84GEO",
        "resCoordType": "WGS84GEO",
        "zoomLevel": 12,
        "trafficType": "AUTO",
        "centerLon": 127.0016985,  # 서울 중심좌표
        "centerLat": 37.5642135
    }

    # API 호출 시 필요한 헤더 설정
    headers = {
        "appKey": "123123123",  # 변경할 것.
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Origin": "https://tmapapi.tmapmobility.com"
    }

    # GET 요청을 통해 교통 정보 요청
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        traffic_data = response.json()
        features = traffic_data.get('features', [])

        # 북위, 남위, 서경, 동경 경계값 설정
        NORTH_LAT = 37.715133
        SOUTH_LAT = 37.413294
        WEST_LON = 126.734086
        EAST_LON = 127.269311

        # 좌표가 범위 내에 있는지 확인하는 함수
        def is_within_boundary(coordinates):
            for lon, lat in coordinates:
                if not (SOUTH_LAT <= lat <= NORTH_LAT and WEST_LON <= lon <= EAST_LON):
                    return False
            return True

        # Firebase에 저장할 데이터를 배열로 저장
        sheet_data = []
        if features:
            first_update_time = features[0]['properties'].get('updateTime', '')

            for feature in features:
                properties = feature.get('properties', {})
                geometry = feature.get('geometry', {})
                coordinates = geometry.get('coordinates', [])

                if properties.get('id') and is_within_boundary(coordinates):
                    coord_str = '; '.join(f'({lon}, {lat})' for lon, lat in coordinates)
                    sheet_data.append({
                        "index": properties.get('index', ''),
                        "id": properties.get('id', ''),
                        "name": properties.get('name', ''),
                        "congestion": properties.get('congestion', ''),
                        "distance": properties.get('distance', ''),
                        "firstUpdateTime": first_update_time,
                        "speed": properties.get('speed', ''),
                        "direction": properties.get('direction', ''),
                        "coordStr": coord_str
                    })

            save_to_firebase(sheet_data)
            print("교통 정보가 성공적으로 Firebase에 저장되었습니다.")
        else:
            print("교통 정보가 없습니다.")
    else:
        print(f"Error: {response.status_code}")

# Firebase에 데이터 저장 함수
def save_to_firebase(data):
  with open(f'./traffic/traffic-{time.time()}.json', 'w') as json_file:
      json.dump(data, json_file)

# 프로그램 실행 예시

start_time = time.time()
collect_and_save_traffic_data()
while True:
    time.sleep(0.5)
    chek_time = time.time()
    if int(chek_time - start_time) > 1200:
      collect_and_save_traffic_data()
      start_time = chek_time # 시간을 다시 초기화

