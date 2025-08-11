const API_BASE_URL = 'http://127.0.0.1:8000';
const appRoot = document.getElementById('app-root');

// --- 1. ФУНКЦИИ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ С API ---

async function getPosts() {
    try {
        const response = await fetch(`${API_BASE_URL}/get_posts`);
        if (!response.ok) throw new Error('Network response was not ok');
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch posts:', error);
        return []; // Возвращаем пустой массив в случае ошибки
    }
}

async function getUsers() {
    try {
        const response = await fetch(`${API_BASE_URL}/get_users`);
        if (!response.ok) throw new Error('Network response was not ok');
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch users:', error);
        return [];
    }
}


// --- 2. ФУНКЦИИ-ШАБЛОНЫ ДЛЯ ОТРИСОВКИ СТРАНИЦ ---

// Шаблон для одного поста в ленте
function createPostCard(post) {
    const postDate = new Date(post.created_at).toLocaleString('ru-RU');
    const authorInitial = post.author.nickname.charAt(0) || '?';

    return `
        <div class="post-card">
            <div class="post-card-header">
                <div class="avatar">${authorInitial}</div>
                <div class="author-info">
                    <p class="nickname">${post.author.nickname}</p>
                    <p class="post-date">${postDate}</p>
                </div>
            </div>
            <div class="post-card-body">
                <h2>${post.title}</h2>
                <p>${post.description}</p>
                ${post.theme ? `<span class="theme">#${post.theme}</span>` : ''}
            </div>
        </div>
    `;
}

// Рендер страницы "Лента"
async function renderFeedPage() {
    appRoot.innerHTML = '<h2>Загрузка ленты...</h2>';
    const posts = await getPosts();
    if (posts.length === 0) {
        appRoot.innerHTML = '<h2>Лента пуста. Создайте первый пост!</h2>';
        return;
    }
    const feedHtml = posts.map(createPostCard).join('');
    appRoot.innerHTML = `<h1>Лента</h1>${feedHtml}`;
}

// Рендер страницы "Создать пост"
async function renderCreatePostPage() {
    const users = await getUsers();
    const userOptions = users.map(user => `<option value="${user.id}">${user.nickname}</option>`).join('');

    appRoot.innerHTML = `
        <div class="form-container">
            <h2>Создать новый пост</h2>
            <form id="create-post-form">
                <select name="user_id" required>
                    <option value="" disabled selected>Выберите автора</option>
                    ${userOptions}
                </select>
                <input type="text" name="title" placeholder="Заголовок" required>
                <textarea name="description" placeholder="Что у вас нового?" rows="5" required></textarea>
                <input type="text" name="theme" placeholder="Тема (например, 'новости')">
                <button type="submit">Опубликовать</button>
            </form>
        </div>
    `;

    // Навешиваем обработчик на новую форму
    document.getElementById('create-post-form').addEventListener('submit', handleCreatePost);
}

// Рендер страницы "Пользователи"
async function renderUsersPage() {
    appRoot.innerHTML = '<h2>Загрузка пользователей...</h2>';
    const users = await getUsers();
    const usersHtml = users.map(user => `
        <div class="post-card" style="margin-bottom: 1rem;">
            <div class="post-card-header">
                 <div class="avatar">${user.nickname.charAt(0)}</div>
                 <p class="nickname" style="font-size: 1.2rem;">${user.nickname}</p>
            </div>
        </div>
    `).join('');
    appRoot.innerHTML = `<h1>Пользователи</h1>${usersHtml}`;
}

// --- 3. ОБРАБОТЧИКИ СОБЫТИЙ ---

async function handleCreatePost(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const params = new URLSearchParams();
    
    // Перебираем formData и добавляем в URL параметры
    for (const [key, value] of formData.entries()) {
        params.append(key, value);
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}/create_post?${params.toString()}`, {
            method: 'POST',
        });
        if (!response.ok) throw new Error('Failed to create post');
        
        // Перенаправляем на главную страницу (ленту) после успеха
        window.location.hash = '#/';

    } catch (error) {
        console.error(error);
        alert('Ошибка при создании поста');
    }
}


// --- 4. РОУТЕР ---

const routes = {
    '/': renderFeedPage,
    '/create-post': renderCreatePostPage,
    '/users': renderUsersPage,
};

function router() {
    // Получаем хэш или используем '/' по умолчанию
    const path = window.location.hash.slice(1) || '/';
    const renderFunction = routes[path];

    if (renderFunction) {
        renderFunction();
    } else {
        appRoot.innerHTML = '<h2>Страница не найдена</h2>';
    }
}

// Слушаем изменения хэша и первоначальную загрузку страницы
window.addEventListener('hashchange', router);
window.addEventListener('load', () => {
    // Устанавливаем хэш по умолчанию, если его нет
    if (!window.location.hash) {
        window.location.hash = '#/';
    }
    router();
});