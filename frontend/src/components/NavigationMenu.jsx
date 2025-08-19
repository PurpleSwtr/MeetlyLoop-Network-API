// frontend/src/components/NavigationMenu.jsx

import React from "react";
import { useNavigate, useLocation } from 'react-router-dom';
import {
  HomeOutlined,
  UserOutlined,
  ProductOutlined,
  CommentOutlined,
  SettingOutlined,
  LogoutOutlined, // 1. Импортируем иконку для выхода
} from "@ant-design/icons";
import { Segmented, ConfigProvider } from "antd";

// 2. Компонент теперь принимает props: isAuthenticated и onLogout
const Menu = ({ isAuthenticated, onLogout }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const activeColor = "#7259F3";

  // 3. Создаем два разных набора опций
  const guestOptions = [
    { label: "Главная", value: "/", icon: <HomeOutlined /> },
    { label: "Аккаунт", value: "/account", icon: <UserOutlined /> },
  ];

  const userOptions = [
    { label: "Главная", value: "/", icon: <HomeOutlined /> },
    { label: "Посты", value: "/posts", icon: <ProductOutlined /> },
    { label: "Пользователи", value: "Users", icon: <CommentOutlined /> },
    { label: "Настройки", value: "Settings", icon: <SettingOutlined /> },
    // Специальная кнопка "Выйти", у которой нет пути, а есть специальное значение
    { label: "Выйти", value: "logout", icon: <LogoutOutlined /> },
  ];

  // 4. Выбираем, какой набор опций показать, в зависимости от статуса авторизации
  const options = isAuthenticated ? userOptions : guestOptions;
  
  // 5. Обновляем обработчик нажатия
  const handleMenuChange = (value) => {
    if (value === 'logout') {
      // Если нажали на "Выйти", вызываем функцию onLogout
      onLogout();
    } else {
      // Иначе, как и раньше, переходим по пути
      navigate(value);
    }
  };

  return (
    <div className="border-2 border-gray-300 rounded-lg mr-7">
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
          value={location.pathname}
          onChange={handleMenuChange} // Используем новый обработчик
          size='large'
          className="border-12 border-white"
        />
      </ConfigProvider>
    </div>
  );
};

export default Menu;