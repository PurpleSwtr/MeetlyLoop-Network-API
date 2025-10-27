// frontend/src/pages/PostsPage.jsx

import { useState, useEffect } from 'react';
import axios from '../api/axios';
import { Spin, Alert } from 'antd';

import CreatePostForm from '../components/CreatePostForm';
import PostCard from '../components/PostCard';

export default function PostsPage() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // useEffect для загрузки постов при первом рендере страницы
  useEffect(() => {
    const fetchPosts = async () => {
      try {
        setLoading(true);
        const response = await axios.get('/api/posts/get_posts');
        setPosts(response.data);
        setError(null);
      } catch (err) {
        console.error("Ошибка при загрузке постов:", err);
        setError("Не удалось загрузить посты. Попробуйте обновить страницу.");
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []); // Пустой массив зависимостей означает, что эффект выполнится один раз

  // Функция для добавления нового поста в начало списка
  const handlePostCreated = (newPost) => {
    setPosts([newPost, ...posts]);
  };

  return (
    <div className="pt-28 px-4 md:px-20 lg:px-40">
      <div className="max-w-3xl mx-auto">
        {/* Форма создания поста */}
        <CreatePostForm onPostCreated={handlePostCreated} />

        {/* Индикатор загрузки */}
        {loading && <div className="text-center"><Spin size="large" /></div>}

        {/* Сообщение об ошибке */}
        {error && <Alert message="Ошибка" description={error} type="error" showIcon />}

        {/* Лента постов */}
        {!loading && !error && (
          <div>
            {posts.length > 0 ? (
              posts.map((post) => <PostCard key={post.id} post={post} />)
            ) : (
              <div className="text-center text-gray-500">
                <p>Постов пока нет. Будьте первым!</p>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}