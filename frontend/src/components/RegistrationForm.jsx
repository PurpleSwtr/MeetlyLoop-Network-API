import { Card, Form, Input, Button, ConfigProvider } from "antd"; // Добавил ConfigProvider, он у вас был

export default function RegForm({ onSuccess }) {
  const handleFormFinish = (values) => {
    console.log('Форма отправлена:', values);
    if (onSuccess) {
      onSuccess();
    }
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
        {/* 👇 ДОБАВЛЯЕМ ЭТОТ DIV С МИНИМАЛЬНОЙ ВЫСОТОЙ 👇 */}
        <div className="min-h-[380px] flex flex-col justify-center">
          <Form layout="vertical" onFinish={handleFormFinish}>
            <Form.Item name="username" label="Имя пользователя">
              <Input placeholder="username" size="large" /> 
            </Form.Item>
            <Form.Item name="email" label="Email">
              <Input type="email" placeholder="email@example.com" size="large" />
            </Form.Item>
            <Form.Item name="password" label="Пароль">
              <Input.Password placeholder="password" size="large" />
            </Form.Item>
            <Form.Item>
              <Button type="primary" htmlType="submit" block size="large">
                Зарегистрироваться
              </Button>
            </Form.Item>
          </Form>
        </div> {/* 👈 И ЗАКРЫВАЕМ ЕГО */}
      </Card>
    </ConfigProvider>
  );
}