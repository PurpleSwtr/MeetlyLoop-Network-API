import React, { useState } from 'react';
import RegForm from "../components/RegistrationForm.jsx";
import SuccessRegSignForm from "../components/SuccessRegSignForm.jsx";

function MainPage() {
  const [isRegistrationComplete, setRegistrationComplete] = useState(false);

  const handleRegistrationSuccess = () => {
    setRegistrationComplete(true);
  };

  return (
    <div className="pt-40 px-20"> 
      {/* Это правильное выравнивание. Оно УЖЕ есть в вашем коде. */}
      <div className="flex justify-between items-start">
        
        {/* 
          👇 УБИРАЕМ ОТСЮДА pt-50. Он не нужен и ломает верстку.
          Общий отступ сверху задает родитель (pt-40).
        */}
        <div>
          <h1 className='pt-40 text-8xl text-meetly tracking-tighter text-balance'>
            MeetlyLoop<span className="animate-pulse">|</span>
          </h1>
          <p className="mt-8 text-xl text-gray-500">
            Ваш новый способ общения.
          </p>
        </div>

        {/* 
          👇 УБИРАЕМ ОТСЮДА pt-12. Он тоже ломает выравнивание.
        */}
        <div className="w-1/3 max-w-sm">
          {isRegistrationComplete ? (
            <SuccessRegSignForm />
          ) : (
            <RegForm onSuccess={handleRegistrationSuccess} />
          )}
        </div>
      </div>
    </div>
  );
}

export default MainPage;