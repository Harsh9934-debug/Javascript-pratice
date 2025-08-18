import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import { Dashboad } from '../components/Dashboad'
import { Landing } from '../components/Landing'

function App(){
  return (
    <BrowserRouter>
        <Routes>
          <Route path="/dashboad" element ={<Dashboad/>} />
           <Route path="/" element ={<Landing/>} />
        </Routes>
    </BrowserRouter>
  )
}

export default App
