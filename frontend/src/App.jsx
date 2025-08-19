// frontend/src/App.jsx

// --- Логика, которую мы добавляем ---
import { useState } from "react";
import { Routes, Route, useNavigate } from 'react-router-dom';
// ------------------------------------

import ComponentHeader from "./components/Header.jsx";
import MainPage from './pages/MainPage.jsx';
import AccountPage from './pages/AccountPage.jsx';
import PostsPage from './pages/PostsPage.jsx';

function App() {
  // --- Новая логика состояния и навигации ---
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const navigate = useNavigate();

  const handleLogin = () => {
    setIsAuthenticated(true);
    navigate('/posts');
  };
  // ----------------------------------------

  // --- ВАША ОРИГИНАЛЬНАЯ И РАБОТАЮЩАЯ ВЕРСТКА ---
  return (
    <div className="flex flex-col h-screen">
      <ComponentHeader />
      <Routes>
        <Route path="/" element={<MainPage />} />
        
        {/* Модифицируем только этот роут, чтобы передать ему функцию */}
        <Route 
          path="/account" 
          element={<AccountPage onLoginSuccess={handleLogin} />} 
        />

        {/* Добавляем новый роут, как и планировалось */}
        <Route path="/posts" element={<PostsPage />} />
      </Routes>
    </div>
  );
  // ---------------------------------------------
} 

export default App;