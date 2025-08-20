import { useState } from "react"

const App = () =>{

  const [ number, setnumber] = useState(10)

  const Increment=() => {
    setnumber(number+10)
  }

  const Decrement = () =>{
    setnumber(number-10)
  }
  return <div>
      <h1>The number is {number}</h1>
      <button onClick={Increment}>Increment</button>
      <button onClick={Decrement}>Decrement</button>
    </div>
  
}
export default App