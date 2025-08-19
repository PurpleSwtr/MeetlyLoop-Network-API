// frontend/src/components/LoginForm.jsx

import { useState } from 'react';
import { Card, Form, Input, Button, ConfigProvider } from "antd";
import axios from 'axios';
import CustomSwitch from "./Switch.jsx"

export default function LoginForm({ onSuccess }) {
  const [errorMessage, setErrorMessage] = useState('');
  const [rememberMe, setRememberMe] = useState(true);

  const handleFormFinish = async (values) => {
    setErrorMessage('');

    // Готовим данные для логина
    const loginData = {
      email: values.email,
      password: values.password, // Имя поля должно быть 'password'
      remember_me_flag: rememberMe,
    };
    
    console.log('Отправляем на бэкенд для логина:', loginData);

    try {
      // ИЗМЕНЕН URL: теперь это эндпоинт для получения токена
      const response = await axios.post('/api/auth/token', loginData);
      console.log('Успешный логин:', response.data);
      if (onSuccess) {
        onSuccess();
      }
    } 
    catch (error) {
      console.error("Не удалось войти:", error);
      if (error.response && error.response.status === 401) {
          setErrorMessage('Неверный логин или пароль.');
      } else {
          setErrorMessage('Ошибка входа. Попробуйте снова.'); 
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
            Войти в аккаунт
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
              name="email" 
              label="Email"
              rules={[
                { required: true, message: 'Введите email!' },
                { type: 'email', message: 'Введите корректный email!' }
              ]}
            >
              <Input type="email" placeholder="email@example.com" size="large" />
            </Form.Item>

            {/* ИЗМЕНЕНО ИМЯ ПОЛЯ: с password_hash на password */}
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
                Войти
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