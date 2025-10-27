// frontend/src/api/axios.js

import axios from 'axios';

// Создаем экземпляр axios с базовой конфигурацией
const api = axios.create({
  // Указываем, что нужно отправлять cookie с каждым запросом
  withCredentials: true, 
});

export default api;