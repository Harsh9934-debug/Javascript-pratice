const express = require('express')
const app = express()

// Middleware
app.use(express.json()) // Parse JSON bodies
app.use(express.urlencoded({ extended: true })) // Parse URL-encoded bodies

// Enable CORS for Postman testing
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

// In-memory data storage (replace with database in production)
let todos = [
    { id: 1, title: "Learn Node.js", description: "Complete Node.js tutorial", completed: false, createdAt: new Date() },
    { id: 2, title: "Build REST API", description: "Create todo REST API", completed: false, createdAt: new Date() },
    { id: 3, title: "Test with Postman", description: "Test all API endpoints", completed: true, createdAt: new Date() }
]
let nextId = 4

// Helper function to find todo by ID
const findTodoById = (id) => todos.find(todo => todo.id === parseInt(id))

// Routes

// GET / - API Info
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

// GET /api/todos/:id - Get single todo
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

// POST /api/todos - Create new todo
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

// PUT /api/todos/:id - Update todo
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

        // Update fields if provided
        if (title !== undefined) todo.title = title.trim()
        if (description !== undefined) todo.description = description.trim()
        if (completed !== undefined) todo.completed = Boolean(completed)
        todo.updatedAt = new Date()

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

// DELETE /api/todos/:id - Delete todo
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

// 404 handler for undefined routes
app.use((req, res) => {
    res.status(404).json({
        success: false,
        message: "Route not found"
    })
})

// Error handling middleware
app.use((error, req, res, next) => {
    console.error(error.stack)
    res.status(500).json({
        success: false,
        message: "Something went wrong!",
        error: error.message
    })
})

const PORT = process.env.PORT || 3000

app.listen(PORT, () => {
    console.log(`🚀 Todo API Server running on http://localhost:${PORT}`)
    console.log(`📋 Test your API endpoints with Postman:`)
    console.log(`   GET    http://localhost:${PORT}/api/todos`)
    console.log(`   POST   http://localhost:${PORT}/api/todos`)
    console.log(`   PUT    http://localhost:${PORT}/api/todos/:id`)
    console.log(`   DELETE http://localhost:${PORT}/api/todos/:id`)
})