import React from "react";

const App = () => {

  var user = "Harsh"

  let changeuser= () => {
    user = "Aryan"
  }

  return (
    <div>
      <h1>Username is {user}</h1>
      <button onClick={changeuser}>Change user </button>
    </div>
  )
}

export default App