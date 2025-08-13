# ./frontend/Dockerfile

# 1. Используем официальный образ Node.js
FROM node:18

# 2. Устанавливаем рабочую директорию
WORKDIR /app

# 3. Копируем package.json и устанавливаем зависимости (оптимизация кэширования)
COPY package*.json ./
RUN npm install

# 4. Копируем остальной код фронтенда
COPY . .

# 5. Открываем порт, на котором работает Vite (по умолчанию 5173)
EXPOSE 5173

# 6. Запускаем dev-сервер с флагом --host (который мы добавили в package.json)
CMD ["npm", "run", "dev"]