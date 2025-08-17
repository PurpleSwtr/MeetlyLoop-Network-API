import React, { useState } from 'react';
import RegForm from "../components/RegistrationForm.jsx";
import SuccessRegSignForm from "../components/SuccessRegSignForm.jsx";
import { Segmented, ConfigProvider } from "antd";
import {
  PlusCircleOutlined,
  LockOutlined,
} from "@ant-design/icons";
function AccountPage() {
  const [isRegistrationComplete, setRegistrationComplete] = useState(false);
  const activeColor = "#7259F3";
  const hoverColor = "#5246d4";

  const handleRegistrationSuccess = () => {
    setRegistrationComplete(true);
  };
  const options = [
  { label: "Зарегестрироваться", value: "/", icon: <PlusCircleOutlined /> },
  { label: "Войти", value: "/account", icon: <LockOutlined /> },
];
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
        size='base'
        className="border-12 border-white"
        block
      />
    </ConfigProvider>
    </div>
        <div className="w-2/3 max-w-sm">
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

export default AccountPage;