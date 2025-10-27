// frontend/src/components/CreatePostForm.jsx

import { Card, Form, Input, Button, ConfigProvider } from "antd";
import axios from '../api/axios';

export default function CreatePostForm({ onPostCreated }) {
  const [form] = Form.useForm(); // Получаем доступ к методам формы

  const handleFinish = async (values) => {
    try {
      const response = await axios.post('/api/posts/create_post', values);
      console.log("Пост успешно создан:", response.data);
      onPostCreated(response.data); // Передаем новый пост наверх
      form.resetFields(); // Очищаем поля формы
    } catch (error) {
      console.error("Ошибка при создании поста:", error);
      // Здесь можно добавить обработку ошибок, например, через antd.message
    }
  };

  return (
    <ConfigProvider theme={{ token: { colorPrimary: "#7259F3" } }}>
      <Card title="Создать новый пост" style={{ marginBottom: '24px' }}>
        <Form form={form} layout="vertical" onFinish={handleFinish}>
          <Form.Item
            name="title"
            label="Заголовок"
            rules={[{ required: true, message: 'Пожалуйста, введите заголовок!' }]}
          >
            <Input placeholder="О чем вы хотите написать?" />
          </Form.Item>
          <Form.Item
            name="description"
            label="Текст поста"
            rules={[{ required: true, message: 'Пожалуйста, введите текст поста!' }]}
          >
            <Input.TextArea rows={4} placeholder="Ваша история..." />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit" block>
              Опубликовать
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </ConfigProvider>
  );
}