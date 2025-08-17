import ComponentHeader from "./components/Header.jsx";
import MainPage from './pages/MainPage.jsx';
import AccountPage from './pages/AccountPage.jsx';

import { Routes, Route } from 'react-router-dom';

function App() {

  return (
    <div className="flex flex-col h-screen">
      <ComponentHeader />
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/account" element={<AccountPage/>}/>
      </Routes>
    </div>
  );
}

export default App;