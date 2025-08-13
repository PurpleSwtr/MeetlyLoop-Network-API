import logo from "../assets/icons/MeetlyLoopUp-Photoroom.png"
import ComponentCard from "./Card.jsx"
import ComponentSearchLine from "./SearchLine.jsx"
import { LinearGradient } from "react-text-gradients"

export default function ComponentHeader() {
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
          <LinearGradient gradient={["to left", "#ff68f0 , #17acff"]}>
            MeetlyLoop
          </LinearGradient>
        </span>
      </div>
      <div className='flex mx-auto my-auto'>
        <ComponentSearchLine className='w-full max-w-xl drop-shadow-lg' />
      </div>
      <div className='drop-shadow-lg'>
        <ComponentCard />
      </div>
    </header>
  )
}
