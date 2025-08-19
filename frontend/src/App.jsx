// frontend/src/App.jsx

import { useState } from "react";
import { Routes, Route, useNavigate } from 'react-router-dom';

import ComponentHeader from "./components/Header.jsx";
import MainPage from './pages/MainPage.jsx';
import AccountPage from './pages/AccountPage.jsx';
import PostsPage from './pages/PostsPage.jsx';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const navigate = useNavigate();

  const handleLogin = () => {
    setIsAuthenticated(true);
    navigate('/posts');
  };

  // --- НОВАЯ ФУНКЦИЯ ВЫХОДА ---
  const handleLogout = () => {
    setIsAuthenticated(false); // Сбрасываем состояние авторизации
    // ВАЖНО: здесь нужно будет добавить запрос к бэкенду для удаления httpOnly cookie
    console.log("Пользователь вышел из системы.");
    navigate('/account'); // Перенаправляем на страницу входа
  };

  return (
    <div className="flex flex-col h-screen">
      {/* Передаем состояние и обе функции в Header */}
      <ComponentHeader isAuthenticated={isAuthenticated} onLogout={handleLogout} />
      
      <Routes>
        <Route path="/" element={<MainPage />} />
        
        <Route 
          path="/account" 
          element={<AccountPage onLoginSuccess={handleLogin} />} 
        />

        <Route path="/posts" element={<PostsPage />} />
      </Routes>
    </div>
  );
}

export default App;