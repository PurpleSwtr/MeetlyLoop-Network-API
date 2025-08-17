import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import { BrowserRouter } from "react-router-dom" // 👈 1. Импортируем роутер
import "./index.css"
import App from "./App.jsx"

// 👇 2. Оборачиваем App в BrowserRouter
createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
)