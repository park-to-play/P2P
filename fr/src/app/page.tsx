'use client';
import HeadMenu from './features/HeadMenu';
import SearchBar from './features/SearchBar';
import Map from './features/Map';
import VisonData from './features/VisonData';
export default function Home() {
  return (
    <section className='flex min-h-screen flex-col items-center body-font bg-white'>
      <div className='justify-end pl-100 bg-slate-400'>
        <HeadMenu />
        <SearchBar />
        <Map />
        <VisonData />
      </div>
    </section>
  );
}
