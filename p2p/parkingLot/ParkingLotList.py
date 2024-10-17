from decouple import config
import pymysql
from math import radians, cos, sin, sqrt, atan2


SEARCH_RADIUS = 500  # 반경 500m 이내
# 주차장 이름 리스트
PARKING_LOT_NAMES = [
    '양화3주차장[양화선착장앞]', '양화1주차장[당산철교 하부]', '양화2주차장[전망카페]',
    '신한드림리버오피스텔 주차장', '여의도한강3주차장(서강대교남단)', '여의도한강2주차장(마포대교남단)',
    '파크원 주차장', 'IFC 서울 주차장', '아이엠(im)증권빌딩', '여의도한강4주차장(여의2교-하부파천교)',
    '당산2동(구)', '롯데마트맥스 영등포점', '당산노외 공영주차장(시)', '영등포제2스포츠센터',
    '코레일유통 본사 사옥 주차장', '당산근린공원 공영(구)', '여의도한강공원1주차장(63빌딩앞)',
    '씨티플라자 주차장', '앵커원', '여의도 사학연금(TP타워)', '영등포구청역 공영주차장(시)',
    '여의도한강5주차장(성모병원앞)', '금융투자협회', '신길환승(5호선)(구)', '영등포 롯데역사 주차장',
    '세미콜론문래', '영등포동제3공영(구)', '홈플러스 영등포점', '문래동공영(구)', 
    '영등포본동제2공영(구)', '도림동 공영주차장(구)', '대림운동장(구)', '대림1동공영(구)'
]

def haversine(lat1, lon1, lat2, lon2):
    """두 지점 간 거리 계산 (Haversine 공식 사용)"""
    R = 6371  # 지구 반지름 (단위: km)
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c * 1000  # 거리(km)를 미터로 변환

def find_nearby_parking(CURRENT_LAT, CURRENT_LNG):
    """지정된 주차장 목록에서 반경 500m 이내의 주차장을 검색하고 정렬"""
    try:
        connection = pymysql.connect(
        host=config("HOST"),
        port=3306,
        user=config("USER_DB"),
        password=config("PASSWORD"),
        database=config("DATABASE"),
        charset=config("CHARSET"),
        )
        with connection.cursor() as cursor:
            # 주차장 이름 리스트를 SQL 쿼리에 사용하기 위해 튜플로 변환
            format_strings = ','.join(['%s'] * len(PARKING_LOT_NAMES))
            query = f"""
                SELECT DISTINCT park_name, park_address, lat, lng 
                FROM tb_parking 
                WHERE park_name IN ({format_strings})
            """
            cursor.execute(query, tuple(PARKING_LOT_NAMES))
            rows = cursor.fetchall()

            # 반경 500m 이내 주차장 필터링
            unique_parking = set()  # 중복 제거용 set
            nearby_parking = []

            for park_name, park_address, plat, plng in rows:
                distance = haversine(CURRENT_LAT, CURRENT_LNG, float(plat), float(plng))
                if distance <= SEARCH_RADIUS:
                    # 주차장 이름과 위도/경도 조합으로 중복 제거
                    key = (park_name, float(plat), float(plng))
                    if key not in unique_parking:
                        unique_parking.add(key)
                        nearby_parking.append((park_name, park_address, float(plat), float(plng), distance))

            # 거리 순으로 정렬
            nearby_parking.sort(key=lambda x: x[4])


            if nearby_parking:
                return nearby_parking
                    
            else:
                return []

    finally:
        connection.close()
