import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom'
import './App.css'
import { Landing } from '../components/Landing'
import { Dashboad } from '../components/Dashboad'

function App(){
  return (
    <div>
        <BrowserRouter>
          <Appbar />
            <Routes>
              <Route path="/dashboad" 
              element ={<Dashboad/>} />
              <Route path="/"
              element ={<Landing/>} />
            </Routes>
        </BrowserRouter>
    </div>
  )
}

function Appbar(){
  const navigate = useNavigate();
  return <div>
       <div>
        <button onClick={() => {navigate("/")}}>Landing page</button>
        <button onClick={() => {navigate("/dashboad")}}>this is the dashboad</button>
      </div>
  </div>

}

export default App
