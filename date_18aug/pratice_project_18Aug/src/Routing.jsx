// This page is just an example to show the Routing and navigating between the pages

import { BrowserRouter, Route, Routes, useNavigate } from 'react-router-dom'
import './App.css'
import { Landing } from '../components/Landing'
import { Dashboad } from '../components/Dashboad'

function Routing(){
  return (
      <BrowserRouter>
        <Appbar />
          <Routes>
            <Route path="/dashboad" element ={<Dashboad/>} />
            <Route path="/" element ={<Landing/>} />
          </Routes>
      </BrowserRouter>
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

export default Routing
