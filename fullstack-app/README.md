# 🚀 Full-Stack Todo Application

A complete full-stack web application built with React frontend and Express.js backend, demonstrating how frontend and backend communicate without a database.

## 🏗️ Architecture Overview

```
┌─────────────────┐    HTTP/API Calls    ┌─────────────────┐
│   React Frontend │ ◄─────────────────► │ Express Backend │
│   (Port 3000)   │                      │   (Port 5000)   │
└─────────────────┘                      └─────────────────┘
         │                                        │
         │                                        │
    Vite Dev Server                        In-Memory Storage
    (Hot Reload)                           (No Database)
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
npm run install-all
```

### 2. Development Mode (Both Frontend & Backend)
```bash
npm run dev
```

### 3. Production Mode
```bash
npm run build-and-start
```

## 📁 Project Structure

```
fullstack-app/
├── backend/
│   ├── server.js          # Express server with API endpoints
│   └── package.json       # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # Main React component
│   │   ├── main.jsx       # React entry point
│   │   ├── index.css      # Styling
│   │   └── services/
│   │       └── api.js     # API communication layer
│   ├── index.html         # HTML template
│   ├── vite.config.js     # Vite configuration with proxy
│   └── package.json       # Frontend dependencies
├── package.json           # Root package.json with scripts
└── README.md             # This file
```

## 🔗 How Frontend and Backend Connect

### 1. **API Communication Layer** (`frontend/src/services/api.js`)
- Uses Axios for HTTP requests
- Configured with base URL `/api` (proxied to backend)
- Handles request/response logging and error handling
- Provides clean interface for all API operations

### 2. **Vite Proxy Configuration** (`frontend/vite.config.js`)
```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:5000',
      changeOrigin: true,
      secure: false,
    }
  }
}
```
- Routes all `/api/*` requests to backend server
- Enables CORS-free development
- Handles hot reloading seamlessly

### 3. **Express CORS Setup** (`backend/server.js`)
```javascript
app.use(cors()); // Enable CORS for frontend communication
app.use(express.json()); // Parse JSON bodies
```
- Allows frontend to make requests to backend
- Handles JSON data parsing
- Serves static files in production

### 4. **API Endpoints**
- `GET /api/todos` - Fetch all todos
- `POST /api/todos` - Create new todo
- `PUT /api/todos/:id` - Update todo
- `DELETE /api/todos/:id` - Delete todo
- `GET /api/health` - Health check

## 🔄 Data Flow

1. **User Action** → React Component
2. **Component** → API Service (`api.js`)
3. **API Service** → HTTP Request (via Axios)
4. **Vite Proxy** → Routes to Express Server
5. **Express Server** → Processes Request
6. **Express Server** → Returns JSON Response
7. **API Service** → Handles Response
8. **React Component** → Updates State
9. **UI** → Re-renders with New Data

## 🛠️ Development Workflow

### Frontend Development
- React with Vite for fast development
- Hot module replacement
- Proxy configuration for API calls
- Modern ES6+ features

### Backend Development
- Express.js server
- RESTful API design
- In-memory data storage
- CORS enabled for frontend

### Communication
- JSON over HTTP
- RESTful API patterns
- Error handling and logging
- Request/response interceptors

## 🌐 Production Deployment

### Build Process
1. Frontend builds to `frontend/dist/`
2. Express serves static files
3. API routes remain functional
4. Single server deployment

### Environment Variables
- `PORT` - Server port (default: 5000)
- `NODE_ENV` - Environment mode

## 🔧 Available Scripts

- `npm run install-all` - Install all dependencies
- `npm run dev` - Start both frontend and backend in development
- `npm run server` - Start only backend server
- `npm run client` - Start only frontend development server
- `npm run build` - Build frontend for production
- `npm run start` - Start production server
- `npm run build-and-start` - Build and start production

## 📊 Features

- ✅ Create, Read, Update, Delete todos
- ✅ Real-time UI updates
- ✅ Error handling and user feedback
- ✅ Responsive design
- ✅ No database required
- ✅ Hot reloading in development
- ✅ Production-ready build

## 🎯 Key Learning Points

1. **API Communication**: How frontend makes HTTP requests to backend
2. **Proxy Configuration**: How Vite routes API calls to backend
3. **CORS Handling**: How to enable cross-origin requests
4. **State Management**: How React state syncs with backend data
5. **Error Handling**: How to handle API errors gracefully
6. **Development vs Production**: Different configurations for each environment

This application demonstrates a complete full-stack architecture without the complexity of a database, making it perfect for learning how frontend and backend communicate!
