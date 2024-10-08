import Image from 'next/image';
import React from 'react';

export default function SearchBar() {
  return (
    <div className=''>
      <div className='flex flex-row bg-white shadow-sm p-1 rounded-md text-black'>
        목적지를 입력하세요
        <Image
          src='/search-interface-symbol.png' // public 폴더 기준 경로
          alt='Search'
          width={100}
          height={100}
          unoptimized
        />
      </div>
    </div>
  );
}
