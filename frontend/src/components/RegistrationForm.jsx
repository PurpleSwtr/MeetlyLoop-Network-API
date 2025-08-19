// frontend/src/components/RegistrationForm.jsx

import { useState } from 'react';
import { Card, Form, Input, Button, ConfigProvider } from "antd";
import axios from 'axios';
import CustomSwitch from "./Switch.jsx"

export default function RegForm({ onSuccess }) {
  const [errorMessage, setErrorMessage] = useState('');
  const [rememberMe, setRememberMe] = useState(true);

  const handleFormFinish = async (values) => {
    setErrorMessage('');

    const registrationData = {
        nickname: values.nickname,
        email: values.email,
        password: values.password,
        description: "", // Описание можно будет добавить в профиле
        remember_me_flag: rememberMe,
    };
    
    console.log('Отправляем на бэкенд:', registrationData);

    try {
      // URL правильный, здесь все хорошо
      const response = await axios.post('/api/users/create_user', registrationData);
      console.log('Успешная регистрация:', response.data);
      if (onSuccess) {
        onSuccess(); // Вызываем колбэк для переключения на экран успеха
      }
    } 
    catch (error) {
      console.error("Не удалось отправить запрос:", error);
      
      // --- УЛУЧШЕННАЯ ЛОГИКА ОБРАБОТКИ ОШИБОК ---
      if (error.response && error.response.status === 409) {
          // Если сервер вернул 409 Conflict
          setErrorMessage('Пользователь с таким email или никнеймом уже существует.');
      } else {
          // Для всех остальных ошибок (нет сети, 500-е и т.д.)
          setErrorMessage('Произошла ошибка. Пожалуйста, попробуйте снова.'); 
      }
    }
  };   

  const handleFormFinishFailed = (errorInfo) => {
    console.log('Validation Failed:', errorInfo);
    setErrorMessage('Пожалуйста, заполните все обязательные поля.');
  };

  const meetlyColor = "#7259F3"; 

  const theme = {
    token: {
      colorPrimary: meetlyColor,
      borderRadius: 6, 
    },
  };

  return (
    <ConfigProvider theme={theme}>
      <Card 
        variant="bordered"
        className='drop-shadow-xl'
        title={
          <div className="text-center text-xl font-semibold text-meetly">
            Создать аккаунт
          </div>
        }
      >
        <div className="min-h-[380px] flex flex-col justify-center">
          <Form 
            layout="vertical" 
            onFinish={handleFormFinish}
            onFinishFailed={handleFormFinishFailed}
          >
            <Form.Item 
              name="nickname" 
              label="Имя пользователя"
              rules={[{ required: true, message: 'Введите имя пользователя!' }]}
            >
              <Input placeholder="username" size="large" /> 
            </Form.Item>

            <Form.Item 
              name="email" 
              label="Email"
              rules={[
                { required: true, message: 'Введите email!' },
                { type: 'email', message: 'Введите корректный email!' }
              ]}
            >
              <Input type="email" placeholder="email@example.com" size="large" />
            </Form.Item>

            <Form.Item 
              name="password" 
              label="Пароль"
              rules={[{ required: true, message: 'Введите пароль!' }]}
            >
              <Input.Password placeholder="password" size="large" />
            </Form.Item>
            
            <Form.Item className="text-right">
            <CustomSwitch checked={rememberMe} onChange={setRememberMe} />
            </Form.Item>
            <Form.Item>
              <Button type="primary" htmlType="submit" block size="large">
                Зарегистрироваться
              </Button>
            </Form.Item>

            {errorMessage && (
              <p className="text-center text-lg text-red-400">
                {errorMessage}
              </p>
            )}
          </Form>
        </div>
      </Card>
    </ConfigProvider>
  );
}