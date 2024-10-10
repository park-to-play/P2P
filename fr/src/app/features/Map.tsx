'use client';
import React, { useEffect, useState } from 'react';
import { KAKAO_API } from '../components/EnvController';

function Map() {
  const [mapSelecter, setMapSelecter] = useState<boolean>(false);

  useEffect(() => {
    // 1. 카카오 지도 초기화
    kakao.maps.load(() => {
      // 2. 지도 생성 및 설정
      const container = document.getElementById('map');
      const options = {
        center: new kakao.maps.LatLng(33.450701, 126.570667),
        level: 3,
      };
      const map = new kakao.maps.Map(container as HTMLElement, options);

      let geocoder = new kakao.maps.services.Geocoder(); // 3. 주소-좌표 변환 객체 생성

      // 4. 지도 상에 주소를 표시
      geocoder.addressSearch(location, function (result, status) {
        if (status === kakao.maps.services.Status.OK) {
          // 5. 결과값으로 받은 위치를 마커로 표시
          const latitude: number = Number(result[0].y);
          const longitude: number = Number(result[0].x);

          let coords = new kakao.maps.LatLng(latitude, longitude);

          // 결과값으로 받은 위치를 마커로 표시
          let marker = new kakao.maps.Marker({
            map: map,
            position: coords,
          });

          let infowindow = new kakao.maps.InfoWindow({
            content: `<div style="width:300px;text-align:center;padding:6px 0;">${(33.450701, 126.570667)}</div>`,
          });
          infowindow.open(map, marker);

          // 6. 지도의 중심을 결과값으로 받은 위치로 이동
          map.setCenter(coords);
          setMapSelecter(true);
        }
      });
    });
  }, []);

  return mapSelecter ? (
    <div>
      <div className='flex items-center justify-center pt-2'>
        <div id='map' className='w-[95%] h-72' />
      </div>
    </div>
  ) : (
    <div className='w-full min-h-max max-w-sm mx-auto p-4'>
      <div className='animate-pulse flex flex-col space-y-4'>
        <div className='bg-gray-300 h-96 w-full rounded-md'></div>
        <div className='flex-1 space-y-2'>
          {/* 제목 스켈레톤 */}
          <div className='h-4 bg-gray-300 rounded w-3/4'></div>
          {/* 지도 설명 스켈레톤 */}
          <div className='h-4 bg-gray-300 rounded w-1/2'></div>
        </div>
      </div>
    </div>
  );
}

export default Map;
