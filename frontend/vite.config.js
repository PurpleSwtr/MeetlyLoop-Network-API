// frontend/vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
  server: {
    proxy: {
      '/api': {
        // --- ФИНАЛЬНОЕ ИСПРАВЛЕНИЕ ---
        // Используем специальное DNS-имя Docker для доступа к хост-машине из контейнера
        target: 'http://host.docker.internal:8000',
        changeOrigin: true,
        secure: false,      
      },
    },
    // Настройки для корректной работы Vite внутри Docker
    host: true, 
    strictPort: true,
    port: 5173,
  }
})