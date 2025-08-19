// frontend/src/components/Header.jsx

import logo from "../assets/icons/MeetlyLoopUp-Photoroom.png"
import ComponentCard from "./NavigationMenu.jsx"
import ComponentSearchLine from "./SearchLine.jsx"
import { LinearGradient } from "react-text-gradients"

// 1. Компонент теперь принимает props
export default function ComponentHeader({ isAuthenticated, onLogout }) {
  return (
    <header
      className='
            flex 
            items-center 
            justify-between 
            absolute 
            w-full 
            z-1 
            bg-[#cecece3b]
          '
    >
      <div className='flex items-center gap-x-1'>
        <img src={logo} alt='Логотип' className='h-25 w-auto' />
        <span className='text-4xl'>
          <LinearGradient gradient={["to left", "#7259F3 , #17acff"]}>
            MeetlyLoop
          </LinearGradient>
        </span>
      </div>
      <div className='flex mx-auto my-auto'>
        <ComponentSearchLine className='w-full max-w-xl drop-shadow-lg border-1 border-gray-300 rounded-lg' />
      </div>
      <div className='drop-shadow-lg'>
        {/* 2. Передаем props дальше в компонент меню */}
        <ComponentCard isAuthenticated={isAuthenticated} onLogout={onLogout} />
      </div>
    </header>
  )
}