import React from 'react';

//  api로 시각화 자료 가져와야함.
function VisonData() {
  return (
    <div className='w-full max-w-sm mx-auto text-center'>
      <div className='animate-pulse flex flex-col space-y-4'>
        <div className='h-4 bg-gray-300 rounded w-3/4'></div>
        <div className='bg-gray-300 h-96 w-full rounded-md items-center'>
          주변 주차장 데이터 불러오기
        </div>
        <div className='h-4 bg-gray-300 rounded w-1/2'></div>
      </div>
    </div>
  );
}

export default VisonData;
