const express = require('express');
const cors = require('cors');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors()); // Enable CORS for frontend communication
app.use(express.json()); // Parse JSON bodies
app.use(express.static(path.join(__dirname, '../frontend/dist'))); // Serve static files

// In-memory data store (no database for simplicity)
let todos = [
  { id: 1, title: 'Learn Full-Stack Development', completed: false },
  { id: 2, title: 'Build a Todo App', completed: true },
  { id: 3, title: 'Deploy to Production', completed: false }
];

let nextId = 4;

// API Routes

// GET /api/todos - Get all todos
app.get('/api/todos', (req, res) => {
  console.log('📝 GET /api/todos - Fetching all todos');
  res.json({
    success: true,
    data: todos,
    message: 'Todos fetched successfully'
  });
});

// POST /api/todos - Create a new todo
app.post('/api/todos', (req, res) => {
  const { title } = req.body;
  
  if (!title || title.trim() === '') {
    return res.status(400).json({
      success: false,
      message: 'Title is required'
    });
  }

  const newTodo = {
    id: nextId++,
    title: title.trim(),
    completed: false
  };

  todos.push(newTodo);
  
  console.log('➕ POST /api/todos - Created new todo:', newTodo);
  
  res.status(201).json({
    success: true,
    data: newTodo,
    message: 'Todo created successfully'
  });
});

// PUT /api/todos/:id - Update a todo
app.put('/api/todos/:id', (req, res) => {
  const { id } = req.params;
  const { title, completed } = req.body;
  const todoId = parseInt(id);

  const todoIndex = todos.findIndex(todo => todo.id === todoId);
  
  if (todoIndex === -1) {
    return res.status(404).json({
      success: false,
      message: 'Todo not found'
    });
  }

  // Update todo properties
  if (title !== undefined) {
    todos[todoIndex].title = title.trim();
  }
  if (completed !== undefined) {
    todos[todoIndex].completed = completed;
  }

  console.log('✏️ PUT /api/todos/:id - Updated todo:', todos[todoIndex]);
  
  res.json({
    success: true,
    data: todos[todoIndex],
    message: 'Todo updated successfully'
  });
});

// DELETE /api/todos/:id - Delete a todo
app.delete('/api/todos/:id', (req, res) => {
  const { id } = req.params;
  const todoId = parseInt(id);

  const todoIndex = todos.findIndex(todo => todo.id === todoId);
  
  if (todoIndex === -1) {
    return res.status(404).json({
      success: false,
      message: 'Todo not found'
    });
  }

  const deletedTodo = todos.splice(todoIndex, 1)[0];
  
  console.log('🗑️ DELETE /api/todos/:id - Deleted todo:', deletedTodo);
  
  res.json({
    success: true,
    data: deletedTodo,
    message: 'Todo deleted successfully'
  });
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({
    success: true,
    message: 'Server is running!',
    timestamp: new Date().toISOString()
  });
});

// Serve React app for all other routes (SPA routing)
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/dist/index.html'));
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('❌ Server Error:', err);
  res.status(500).json({
    success: false,
    message: 'Internal server error'
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
  console.log(`📊 API endpoints available at http://localhost:${PORT}/api/`);
  console.log(`🏥 Health check: http://localhost:${PORT}/api/health`);
});
