import React from 'react';
import { CheckOutlined, CloseOutlined } from '@ant-design/icons';
import { Space, Switch, ConfigProvider } from 'antd';

const CustomSwitch = ({ checked, onChange }) => (
  <ConfigProvider
    theme={{
      components: {
        Switch: {
          colorPrimaryHover: "#5fb518",
          colorPrimary: "#b0db7a",
        },
      },
    }}
  >
    {/* 1. Space теперь горизонтальный и центрированный по вертикали */}
    <Space align="center"> 
      {/* 2. Текст обернут в span для стилизации и добавлен отступ */}
      <span className="text-gray-600 mr-1 text-base font-stretch-50%" >
        Запомнить меня
      </span>
      <Switch
        checkedChildren={<CheckOutlined />}
        unCheckedChildren={<CloseOutlined />}
        checked={checked} 
        onChange={onChange}
        // 3. Убран 'size="small"', чтобы переключатель был стандартного размера
      />
    </Space>
  </ConfigProvider>
);

export default CustomSwitch;