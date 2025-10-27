// frontend/src/App.jsx

import { useState } from "react";
import { Routes, Route, useNavigate } from 'react-router-dom';
import axios from './api/axios'; // <-- Импортируем наш настроенный axios

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

  const handleLogout = async () => {
    try {
      // Отправляем запрос на бэкенд для удаления cookie
      await axios.post('/api/auth/logout');
      console.log("Successfully logged out from backend.");
    } catch (error) {
      console.error("Error during logout:", error);
    } finally {
      // Независимо от ответа сервера, выходим на фронтенде
      setIsAuthenticated(false);
      navigate('/account');
    }
  };

  return (
    <div className="flex flex-col h-screen">
      <ComponentHeader isAuthenticated={isAuthenticated} onLogout={handleLogout} />
      
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/account" element={<AccountPage onLoginSuccess={handleLogin} />} />
        <Route path="/posts" element={<PostsPage />} />
      </Routes>
    </div>
  );
}

export default App;