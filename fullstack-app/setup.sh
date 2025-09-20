#!/bin/bash

echo "🚀 Setting up Full-Stack Todo Application..."
echo "=============================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi

echo "✅ Node.js found: $(node --version)"

# Install root dependencies
echo "📦 Installing root dependencies..."
npm install

# Install backend dependencies
echo "📦 Installing backend dependencies..."
cd backend
npm install
cd ..

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the application:"
echo "  Development mode: npm run dev"
echo "  Production mode:  npm run build-and-start"
echo ""
echo "The application will be available at:"
echo "  Frontend: http://localhost:3000"
echo "  Backend API: http://localhost:5000/api"
echo ""
echo "Happy coding! 🚀"
