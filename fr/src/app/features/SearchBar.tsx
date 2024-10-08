'use client';
import Image from 'next/image';
import React, { useState } from 'react';
import apiSearch from '../services/apiSearch';

function getData(destination: string) {
  const destination_list = apiSearch(destination, 'POST');
  return destination_list;
}

export default function SearchBar() {
  const [destination, setDestination] = useState<string>('');
  console.log(destination);
  return (
    <div className='w-full max-w-sm mx-auto'>
      <div className='flex flex-row items-center bg-white shadow-lg p-3 rounded-lg text-gray-800 border border-gray-200 hover:shadow-xl transition-shadow duration-300 ease-in-out'>
        <input
          type='text'
          placeholder='목적지를 입력하세요'
          onChange={(ans) => {
            setDestination(ans.target.value);
          }}
          className='flex-1 bg-transparent outline-none text-gray-700 placeholder-gray-400 px-2'
        />
        <button
          onClick={() => {
            getData(destination);
          }}
          className='ml-3 p-2 bg-blue-500 hover:bg-blue-600 text-white rounded-full transition-colors duration-300 ease-in-out'
        >
          <Image
            src='/config/search-interface-symbol.png'
            alt='Search'
            width={16}
            height={16}
          />
        </button>
      </div>
    </div>
  );
}
