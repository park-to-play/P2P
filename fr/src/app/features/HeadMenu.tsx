import React from 'react';

function HeadMenu() {
  return (
    <div className='p-4 sm:p-6 md:p-8 lg:p-12 bg-slate-600 flex-row'>
      <h1 className='text-lg sm:text-xl md:text-2xl lg:text-3xl'>ParkToPlay</h1>
      <p className='text-sm sm:text-base md:text-l text-yellow-500'>Login</p>
    </div>
  );
}

export default HeadMenu;
