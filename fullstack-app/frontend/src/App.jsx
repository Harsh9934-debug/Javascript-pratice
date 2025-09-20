import React, { useState, useEffect } from 'react';
import { todoAPI } from './services/api';
import './index.css';

function App() {
  // State management
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [editingId, setEditingId] = useState(null);
  const [editingText, setEditingText] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  // Load todos on component mount
  useEffect(() => {
    loadTodos();
  }, []);

  // Load todos from API
  const loadTodos = async () => {
    try {
      setLoading(true);
      setError('');
      const response = await todoAPI.getAllTodos();
      setTodos(response.data);
      console.log('📝 Loaded todos:', response.data);
    } catch (err) {
      setError(err.message);
      console.error('❌ Error loading todos:', err);
    } finally {
      setLoading(false);
    }
  };

  // Create new todo
  const handleAddTodo = async (e) => {
    e.preventDefault();
    if (!newTodo.trim()) return;

    try {
      setError('');
      const response = await todoAPI.createTodo(newTodo.trim());
      setTodos(prev => [...prev, response.data]);
      setNewTodo('');
      setSuccess('Todo added successfully!');
      setTimeout(() => setSuccess(''), 3000);
      console.log('➕ Created todo:', response.data);
    } catch (err) {
      setError(err.message);
      console.error('❌ Error creating todo:', err);
    }
  };

  // Toggle todo completion
  const handleToggleTodo = async (id, completed) => {
    try {
      setError('');
      const response = await todoAPI.updateTodo(id, { completed: !completed });
      setTodos(prev => 
        prev.map(todo => 
          todo.id === id ? response.data : todo
        )
      );
      console.log('✏️ Toggled todo:', response.data);
    } catch (err) {
      setError(err.message);
      console.error('❌ Error toggling todo:', err);
    }
  };

  // Start editing todo
  const handleStartEdit = (id, title) => {
    setEditingId(id);
    setEditingText(title);
  };

  // Save edited todo
  const handleSaveEdit = async (id) => {
    if (!editingText.trim()) return;

    try {
      setError('');
      const response = await todoAPI.updateTodo(id, { title: editingText.trim() });
      setTodos(prev => 
        prev.map(todo => 
          todo.id === id ? response.data : todo
        )
      );
      setEditingId(null);
      setEditingText('');
      setSuccess('Todo updated successfully!');
      setTimeout(() => setSuccess(''), 3000);
      console.log('✏️ Updated todo:', response.data);
    } catch (err) {
      setError(err.message);
      console.error('❌ Error updating todo:', err);
    }
  };

  // Cancel editing
  const handleCancelEdit = () => {
    setEditingId(null);
    setEditingText('');
  };

  // Delete todo
  const handleDeleteTodo = async (id) => {
    if (!window.confirm('Are you sure you want to delete this todo?')) return;

    try {
      setError('');
      await todoAPI.deleteTodo(id);
      setTodos(prev => prev.filter(todo => todo.id !== id));
      setSuccess('Todo deleted successfully!');
      setTimeout(() => setSuccess(''), 3000);
      console.log('🗑️ Deleted todo:', id);
    } catch (err) {
      setError(err.message);
      console.error('❌ Error deleting todo:', err);
    }
  };

  // Render todo item
  const renderTodoItem = (todo) => {
    if (editingId === todo.id) {
      return (
        <li key={todo.id} className="todo-item">
          <input
            type="text"
            value={editingText}
            onChange={(e) => setEditingText(e.target.value)}
            className="todo-input"
            autoFocus
            onKeyPress={(e) => e.key === 'Enter' && handleSaveEdit(todo.id)}
          />
          <div className="todo-actions">
            <button 
              onClick={() => handleSaveEdit(todo.id)}
              className="edit-btn"
            >
              Save
            </button>
            <button 
              onClick={handleCancelEdit}
              className="delete-btn"
            >
              Cancel
            </button>
          </div>
        </li>
      );
    }

    return (
      <li key={todo.id} className="todo-item">
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={() => handleToggleTodo(todo.id, todo.completed)}
          className="todo-checkbox"
        />
        <span className={`todo-text ${todo.completed ? 'completed' : ''}`}>
          {todo.title}
        </span>
        <div className="todo-actions">
          <button 
            onClick={() => handleStartEdit(todo.id, todo.title)}
            className="edit-btn"
          >
            Edit
          </button>
          <button 
            onClick={() => handleDeleteTodo(todo.id)}
            className="delete-btn"
          >
            Delete
          </button>
        </div>
      </li>
    );
  };

  return (
    <div className="container">
      <div className="header">
        <h1>🚀 Full-Stack Todo App</h1>
        <p>Built with React + Express + No Database</p>
      </div>

      {/* Success/Error Messages */}
      {success && <div className="success">{success}</div>}
      {error && <div className="error">{error}</div>}

      {/* Add Todo Form */}
      <form onSubmit={handleAddTodo} className="todo-form">
        <input
          type="text"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          placeholder="Add a new todo..."
          className="todo-input"
          disabled={loading}
        />
        <button 
          type="submit" 
          className="add-btn"
          disabled={loading || !newTodo.trim()}
        >
          Add Todo
        </button>
      </form>

      {/* Todo List */}
      {loading ? (
        <div className="loading">Loading todos...</div>
      ) : todos.length === 0 ? (
        <div className="empty-state">
          <h3>No todos yet!</h3>
          <p>Add your first todo above to get started.</p>
        </div>
      ) : (
        <ul className="todo-list">
          {todos.map(renderTodoItem)}
        </ul>
      )}

      {/* Connection Status */}
      <div style={{ marginTop: '20px', textAlign: 'center', fontSize: '0.9rem', color: '#666' }}>
        <p>🔄 Frontend ↔️ Backend Connection Active</p>
        <p>API Base URL: <code>/api</code> (proxied to localhost:5000)</p>
      </div>
    </div>
  );
}

export default App;
