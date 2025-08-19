// frontend/src/components/SuccessRegSignForm.jsx

import React from 'react';
import { Card, Button, ConfigProvider } from 'antd';

const CheckIcon = () => (
  <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M5 13l4 4L19 7"></path>
  </svg>
);

// --- ИЗМЕНЕНИЯ ЗДЕСЬ ---
// Добавляем props с значениями по умолчанию для обратной совместимости
export default function SuccessRegSignForm({
  title = "Аккаунт создан!",
  message = "Теперь вы можете войти, используя свои данные.",
  buttonText = "Перейти ко входу",
  onContinue,
}) {
  const successColor = '#5fb518';
  const successColorHover = '#4a9413';

  return (
    <Card variant="bordered" className='drop-shadow-xl w-full'>
      <div className="min-h-[380px] flex flex-col items-center p-8 text-center">
        
        <div>
          <div className="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-meetly">
            <CheckIcon />
          </div>
          {/* Используем props для текста */}
          <h2 className="mt-6 text-3xl font-bold text-meetly">
            {title}
          </h2>
          <p className="mt-2 text-base text-gray-500 max-w-xs">
            {message}
          </p>
        </div>
        
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
              onClick={onContinue}
            >
              {buttonText}
            </Button>
          </ConfigProvider>
        </div>
      </div>
    </Card>
  );
}