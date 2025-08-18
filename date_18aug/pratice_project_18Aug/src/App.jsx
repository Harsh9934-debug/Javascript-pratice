import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import { Dashboad } from '../components/Dashboad'
import { Landing } from '../components/Landing'

function App(){
  return (
    <div>
      <div>
        <button onClick={() => {window.location.href = "/"}}>Landing page</button>
        <button onClick={() => {window.location.href = "/dashboad"}}>this is the dashboad</button>
      </div>
      <BrowserRouter>
          <Routes>
            <Route path="/dashboad" element ={<Dashboad/>} />
            <Route path="/" element ={<Landing/>} />
          </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
