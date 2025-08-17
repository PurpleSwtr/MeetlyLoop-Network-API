import React, { useState } from "react";
import { Link, useNavigate, useLocation } from 'react-router-dom';

import {
  HomeOutlined,
  UserOutlined,
  ProductOutlined,
  CommentOutlined,
  SettingOutlined,
} from "@ant-design/icons";
import { Segmented, ConfigProvider } from "antd";

const options = [
  { label: "Главная", value: "/", icon: <HomeOutlined /> },
  { label: "Аккаунт", value: "/account", icon: <UserOutlined /> },
  { label: "Посты", value: "Posts", icon: <ProductOutlined /> },
  { label: "Пользователи", value: "Users", icon: <CommentOutlined /> },
  { label: "Настройки", value: "Settings", icon: <SettingOutlined /> },
];

const Menu = () => {
  const navigate = useNavigate();
  const location = useLocation();
  
  const activeColor = "#7259F3";

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
        onChange={(value) => navigate(value)}
        size='large'
        className="border-12 border-white"
      />
    </ConfigProvider>
    </div>
  );
};
export default Menu;