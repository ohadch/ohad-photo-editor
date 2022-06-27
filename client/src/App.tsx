import './App.css'
import FileUploaderContainer from "./components/FileUploaderContainer/FileUploaderContainer";

function App() {
  return (
    <div className="App">
        <div className={"content"}>
            <h1>Cartoonizer</h1>
            <FileUploaderContainer />
        </div>
    </div>
  )
}

export default App
