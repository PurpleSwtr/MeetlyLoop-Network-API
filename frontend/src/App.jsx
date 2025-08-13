import ComponentHeader from "./components/Header.jsx";
import PageMain from "./pages/MainPage.jsx"

function App() {
  return (
    <div className="flex flex-col h-screen">
      <ComponentHeader />
        <PageMain/>
    </div>
  );
}

export default App;