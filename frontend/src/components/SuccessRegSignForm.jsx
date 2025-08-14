import React from 'react';
import { Card, Button, ConfigProvider } from 'antd'; // Убрали ненужный Form

const CheckIcon = () => (
  <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M5 13l4 4L19 7"></path>
  </svg>
);

export default function SuccessRegSignForm() {
  const successColor = '#5fb518';
  const successColorHover = '#4a9413';

  return (
    <Card variant="bordered" className='drop-shadow-xl w-full'>
      {/* 
        Основной контейнер. flex-col и min-h создают пространство.
        p-8 создаёт отступы по краям.
      */}
      <div className="min-h-[380px] flex flex-col items-center p-8 text-center">
        
        {/* === ВЕРХНИЙ БЛОК === */}
        {/* Он остаётся наверху, потому что он первый в потоке */}
        <div>
          <div className="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-meetly">
            <CheckIcon />
          </div>
          
          <h2 className="mt-6 text-3xl font-bold text-meetly">
            Аккаунт создан!
          </h2>

          <p className="mt-2 text-base text-gray-500 max-w-xs">
            Теперь вы можете войти, используя свои данные.
          </p>
        </div>
        
        {/* 
          === НИЖНИЙ БЛОК (КНОПКА) ===
          👇👇👇 ВСЯ МАГИЯ ЗДЕСЬ 👇👇👇
          Мы оборачиваем кнопку в простой <div> и даём ему класс mt-auto.
          Этот div становится flex-элементом, который отталкивается от верхнего блока
          и прижимается к низу контейнера.
        */}
        <div className="w-full mt-20">
          <ConfigProvider
            theme={{
              token: {
                colorPrimary: successColor, 
                colorPrimaryHover: successColorHover,
              }
            }}
          >
            <Button 
              type="primary"
              block
              size="large"
            >
              Продолжить
            </Button>
          </ConfigProvider>
        </div>

      </div>
    </Card>
  );
}