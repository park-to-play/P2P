import React from 'react';

function HeadMenu() {
  return (
    <div className='w-full max-w-sm mx-auto'>
      <h1 className='text-lg sm:text-xl md:text-2xl lg:text-3xl flex flex-row'>
        ParkToPlay
        <p className='ml-auto text-sm sm:text-base md:text-l text-yellow-500'>
          Login
        </p>
      </h1>
    </div>
  );
}

export default HeadMenu;
