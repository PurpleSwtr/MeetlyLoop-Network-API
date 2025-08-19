// frontend/src/pages/AccountPage.jsx

import React, { useState } from 'react';
import RegForm from "../components/RegistrationForm.jsx";
import SuccessRegSignForm from "../components/SuccessRegSignForm.jsx";
import LoginForm from "../components/LoginForm.jsx";

import { Segmented, ConfigProvider } from "antd";
import { PlusCircleOutlined, LockOutlined } from "@ant-design/icons";

// --- ИЗМЕНЕНИЕ ЗДЕСЬ ---
// Получаем новый пропс onLoginSuccess от App.jsx
function AccountPage({ onLoginSuccess }) {
  const activeColor = "#7259F3";
  const [pageState, setPageState] = useState('registration');

  // Управляем состояниями
  const handleRegistrationSuccess = () => setPageState('registration_success');
  const handleLoginSuccess = () => setPageState('login_success'); // Новое состояние
  const switchToLogin = () => setPageState('login');

  const componentsMap = {
    registration: <RegForm onSuccess={handleRegistrationSuccess} />,
    
    // Передаем handleLoginSuccess в LoginForm
    login: <LoginForm onSuccess={handleLoginSuccess} />,
    
    // Экран успеха после РЕГИСТРАЦИИ
    registration_success: <SuccessRegSignForm onContinue={switchToLogin} />,

    // --- НОВЫЙ КОМПОНЕНТ В КАРТЕ ---
    // Экран успеха после ВХОДА
    login_success: (
      <SuccessRegSignForm
        title="Вы успешно вошли!"
        message="Сейчас вы будете перенаправлены на главную страницу."
        buttonText="Продолжить"
        onContinue={onLoginSuccess} // Вызываем функцию из App.jsx для редиректа!
      />
    ),
  };

  const options = [
    { label: "Зарегистрироваться", value: "registration", icon: <PlusCircleOutlined /> },
    { label: "Войти", value: "login", icon: <LockOutlined /> },
  ];
  
  // Определяем активную вкладку для Segmented
  let activeTab = pageState;
  if (pageState === 'registration_success') activeTab = 'login';
  if (pageState === 'login_success') activeTab = 'login';


  return (
    <div className="pt-30 px-20"> 
      <div className="flex flex-col items-center">
        <div className="w-2/3 max-w-sm border-2 border-gray-300 rounded-lg mb-1">
          <ConfigProvider
            theme={{
              components: {
                Segmented: {
                  itemSelectedBg: activeColor,
                  itemSelectedColor: "#fff",
                  trackBg: "#ffffff",
                },
              },
            }}
          >
            <Segmented
              options={options}
              value={activeTab} // Используем вычисленную активную вкладку
              onChange={(value) => setPageState(value)}
              size='middle'
              className="border-12 border-white"
              block
            />
          </ConfigProvider>
        </div>
        <div className="w-2/3 max-w-sm">
          {componentsMap[pageState] || <div>Ошибка состояния</div>}
        </div>
      </div>
    </div>
  );
}

export default AccountPage;