'use client';
import HeadMenu from './features/HeadMenu';
import SearchBar from './features/SearchBar';
import Map from './features/Map';
import VisonData from './features/VisonData';
import Advertisement from './features/Advertisement';
import Connect from './features/Connect';
export default function Home() {
  return (
    <section className='flex flex-col min-h-screen items-center body-font bg-gray-100'>
      <div className='w-full md:max-w-[60%] mx-auto bg-slate-400 p-4 sm:p-6'>
        <HeadMenu />
        <SearchBar />
        <Map />
        <Advertisement />
        <VisonData />
        <Connect />
      </div>
    </section>
  );
}
