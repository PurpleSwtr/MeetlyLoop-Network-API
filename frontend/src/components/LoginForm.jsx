import { useState } from 'react'; // 👈 1. Импортируем useState
import { Card, Form, Input, Button, ConfigProvider } from "antd";
import axios from 'axios';
import CustomSwitch from "./Switch.jsx"

export default function LoginForm({ onSuccess }) {
  const [errorMessage, setErrorMessage] = useState('');
  const [rememberMe, setRememberMe] = useState(true);

  const handleFormFinish = async (values) => {
    setErrorMessage('');

    values.description = "";
    values.remember_me_flag = rememberMe;
    
    console.log('Отправляем на бэкенд:', values);

    try {
      const response = await axios.post('/api/create_user', values);
      console.log('response:', response.data);
      if (onSuccess) {
        onSuccess();
      }
    } 
    catch (error) {
      console.error("Не удалось отправить запрос:", error);
      // Показываем ошибку, если что-то пошло не так на сервере
      setErrorMessage('Ошибка регистрации. Попробуйте снова.'); 
    }
  };   

  // 3. Этот обработчик сработает, если валидация НЕ пройдена
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

            <Form.Item 
              name="password_hash" 
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