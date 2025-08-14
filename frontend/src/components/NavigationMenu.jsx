import React, { useState } from "react";
import {
  HomeOutlined,
  UserOutlined,
  ProductOutlined,
  CommentOutlined,
  SettingOutlined,
} from "@ant-design/icons";
import { Segmented, ConfigProvider } from "antd";

const options = [
  { label: "Главная", value: "Home", icon: <HomeOutlined /> },
  { label: "Аккаунт", value: "Account", icon: <UserOutlined /> },
  { label: "Посты", value: "Posts", icon: <ProductOutlined /> },
  { label: "Пользователи", value: "Users", icon: <CommentOutlined /> },
  { label: "Настройки", value: "Settings", icon: <SettingOutlined /> },
];

const Demo = ({ onMenuChanged }) => {
  const [selectedValue, setSelectedValue] = useState("Home");
  console.log("", selectedValue);
  const activeColor = "#7259F3";

  return (
    <div className="border border-gray-300 rounded-lg mr-7">
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
        value={selectedValue}
        onChange={setSelectedValue}
        size='large'
        className="border-12 border-white"
      />
    </ConfigProvider>
    </div>

  );

  
};
// p-2 border border-gray-300 rounded-lg
export default Demo;