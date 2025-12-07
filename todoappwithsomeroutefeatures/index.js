const express = require('express')
const app = express()

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

const fs = require('fs')
const path = require('path')


const TODOS_FILE = path.join(__dirname, 'todos.json')


const saveToFile = () => {
    try {
        fs.writeFileSync(TODOS_FILE, JSON.stringify(todos, null, 2))
        console.log(' Data saved to todos.json')
    } catch (error) {
        console.error(' Error saving data:', error.message)
    }
}

const loadFromFile = () => {
    try {
        if (fs.existsSync(TODOS_FILE)) {
            const data = fs.readFileSync(TODOS_FILE, 'utf8')
            const loadedTodos = JSON.parse(data)
            

            loadedTodos.forEach(todo => {
                todo.createdAt = new Date(todo.createdAt)
                if (todo.updatedAt) {
                    todo.updatedAt = new Date(todo.updatedAt)
                }
            })
            
            todos = loadedTodos
            

            nextId = todos.length > 0 ? Math.max(...todos.map(t => t.id)) + 1 : 1
            
            console.log(` Loaded ${todos.length} todos from file`)
        } else {
            console.log(' No existing data file, using default todos')
            saveToFile()
        }
    } catch (error) {
        console.error(' Error loading data:', error.message)
        console.log(' Using default todos')
    }
}


app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*')
    res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization')
    if (req.method === 'OPTIONS') {
        res.sendStatus(200)
    } else {
        next()
    }
})

let todos = [
    { id: 1, title: "Learn Node.js", description: "Complete Node.js tutorial", completed: false, createdAt: new Date() },
    { id: 2, title: "Build REST API", description: "Create todo REST API", completed: false, createdAt: new Date() },
    { id: 3, title: "Test with Postman", description: "Test all API endpoints", completed: true, createdAt: new Date() }
]
let nextId = 4

const findTodoById = (id) => todos.find(todo => todo.id === parseInt(id))

app.get('/', (req, res) => {
    res.json({
        message: "Todo API Server",
        version: "1.0.0",
        endpoints: {
            "GET /": "API information",
            "GET /api/todos": "Get all todos",
            "GET /api/todos/:id": "Get todo by ID",
            "POST /api/todos": "Create new todo",
            "PUT /api/todos/:id": "Update todo by ID", 
            "DELETE /api/todos/:id": "Delete todo by ID"
        }
    })
})

// GET /api/todos - Get all todos
app.get('/api/todos', (req, res) => {
    try {
        res.status(200).json({
            success: true,
            count: todos.length,
            data: todos
        })
    } catch (error) {
        res.status(500).json({
            success: false,
            message: "Server error",
            error: error.message
        })
    }
})


app.get('/api/todos/:id', (req, res) => {
    try {
        const todo = findTodoById(req.params.id)
        
        if (!todo) {
            return res.status(404).json({
                success: false,
                message: "Todo not found"
            })
        }

        res.status(200).json({
            success: true,
            data: todo
        })
    } catch (error) {
        res.status(500).json({
            success: false,
            message: "Server error",
            error: error.message
        })
    }
})


app.post('/api/todos', (req, res) => {
    try {
        const { title, description } = req.body

        // Validation
        if (!title || title.trim() === '') {
            return res.status(400).json({
                success: false,
                message: "Title is required"
            })
        }

        // Create new todo
        const newTodo = {
            id: nextId++,
            title: title.trim(),
            description: description ? description.trim() : '',
            completed: false,
            createdAt: new Date()
        }

        todos.push(newTodo)
        saveToFile() 

        res.status(201).json({
            success: true,
            message: "Todo created successfully",
            data: newTodo
        })
    } catch (error) {
        res.status(500).json({
            success: false,
            message: "Server error",
            error: error.message
        })
    }
})


app.put('/api/todos/:id', (req, res) => {
    try {
        const todo = findTodoById(req.params.id)
        
        if (!todo) {
            return res.status(404).json({
                success: false,
                message: "Todo not found"
            })
        }

        const { title, description, completed } = req.body


        if (title !== undefined) todo.title = title.trim()
        if (description !== undefined) todo.description = description.trim()
        if (completed !== undefined) todo.completed = Boolean(completed)
        todo.updatedAt = new Date()
        
        saveToFile() 

        res.status(200).json({
            success: true,
            message: "Todo updated successfully",
            data: todo
        })
    } catch (error) {
        res.status(500).json({
            success: false,
            message: "Server error",
            error: error.message
        })
    }
})

app.delete('/api/todos/:id', (req, res) => {
    try {
        const todoIndex = todos.findIndex(todo => todo.id === parseInt(req.params.id))
        
        if (todoIndex === -1) {
            return res.status(404).json({
                success: false,
                message: "Todo not found"
            })
        }

        const deletedTodo = todos.splice(todoIndex, 1)[0]
        saveToFile() 

        res.status(200).json({
            success: true,
            message: "Todo deleted successfully",
            data: deletedTodo
        })
    } catch (error) {
        res.status(500).json({
            success: false,
            message: "Server error",
            error: error.message
        })
    }
})


app.use((req, res) => {
    res.status(404).json({
        success: false,
        message: "Route not found"
    })
})


app.use((error, req, res, next) => {
    console.error(error.stack)
    res.status(500).json({
        success: false,
        message: "Something went wrong!",
        error: error.message
    })
})

const PORT = process.env.PORT || 3000


loadFromFile()

app.listen(PORT, () => {
    console.log(`Todo API Server running on http://localhost:${PORT}`)
    console.log(`Data persistence: Enabled (JSON file storage)`)
    console.log(`Test your API endpoints with Postman:`)
    console.log(`   GET    http://localhost:${PORT}/api/todos`)
    console.log(`   POST   http://localhost:${PORT}/api/todos`)
    console.log(`   PUT    http://localhost:${PORT}/api/todos/:id`)
    console.log(`   DELETE http://localhost:${PORT}/api/todos/:id`)
})