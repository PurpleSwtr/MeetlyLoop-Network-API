// frontend/src/components/PostCard.jsx

import { Card, Avatar } from 'antd';
import { UserOutlined } from '@ant-design/icons';

const { Meta } = Card;

// Функция для форматирования даты
const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(dateString).toLocaleDateString('ru-RU', options);
};

export default function PostCard({ post }) {
  return (
    <Card style={{ marginBottom: '24px' }}>
      <Meta
        avatar={<Avatar icon={<UserOutlined />} />}
        title={post.author.nickname}
        description={`Опубликовано: ${formatDate(post.updated_at)}`}
      />
      <div style={{ marginTop: '16px' }}>
        <h3 className="text-2xl font-bold mb-2">{post.title}</h3>
        <p className="text-gray-700">{post.description}</p>
      </div>
    </Card>
  );
}