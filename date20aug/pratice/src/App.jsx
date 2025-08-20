import React, { useState } from "react";

const App = () => {

  const [a, setA] = useState(10)

  const changeA =() =>{
    setA (20)
  }
  return (
    <div>
      <h1>Username is {a}</h1>
      <button onClick={changeA}>change A</button>
    </div>
  )
}

export default App