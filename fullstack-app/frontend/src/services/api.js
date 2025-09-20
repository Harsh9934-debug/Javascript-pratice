import axios from 'axios';

// Create axios instance with base configuration
const api = axios.create({
  baseURL: '/api', // This will be proxied to http://localhost:5000/api
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log(`🚀 API Request: ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('❌ API Request Error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for logging and error handling
api.interceptors.response.use(
  (response) => {
    console.log(`✅ API Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    console.error('❌ API Response Error:', error.response?.status, error.message);
    
    // Handle different error types
    if (error.response) {
      // Server responded with error status
      const message = error.response.data?.message || 'Server error occurred';
      return Promise.reject(new Error(message));
    } else if (error.request) {
      // Request was made but no response received
      return Promise.reject(new Error('Network error - please check your connection'));
    } else {
      // Something else happened
      return Promise.reject(new Error('An unexpected error occurred'));
    }
  }
);

// API functions for todos
export const todoAPI = {
  // Get all todos
  getAllTodos: async () => {
    const response = await api.get('/todos');
    return response.data;
  },

  // Create a new todo
  createTodo: async (title) => {
    const response = await api.post('/todos', { title });
    return response.data;
  },

  // Update a todo
  updateTodo: async (id, updates) => {
    const response = await api.put(`/todos/${id}`, updates);
    return response.data;
  },

  // Delete a todo
  deleteTodo: async (id) => {
    const response = await api.delete(`/todos/${id}`);
    return response.data;
  },

  // Health check
  healthCheck: async () => {
    const response = await api.get('/health');
    return response.data;
  }
};

export default api;
