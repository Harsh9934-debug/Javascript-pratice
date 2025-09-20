import { useState } from "react"
import "./index.css"

const App = () => {
  const [number, setNumber] = useState(10)


  
  const Increment = () => {
    setNumber(number + 10)
  }

  const Decrement = () => {
    setNumber(number - 10)
  }

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100 text-gray-900">
      <h1 className="text-3xl font-bold mb-6">
        The number is <span className="text-indigo-600">{number}</span>
      </h1>
      <div className="space-x-4">
        <button
          onClick={Increment}
          className="px-6 py-2 bg-green-500 text-white rounded-lg shadow hover:bg-green-600 transition"
        >
          Increment
        </button>
        <button
          onClick={Decrement}
          className="px-6 py-2 bg-red-500 text-white rounded-lg shadow hover:bg-red-600 transition"
        >
          Decrement
        </button>
      </div>
    </div>
  )
}

export default App
