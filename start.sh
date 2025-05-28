#!/bin/bash

# BlockBoss Flask App Startup Script

echo "🚀 Starting BlockBoss Landing Page..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Start the Flask app
echo "🌐 Starting Flask server at http://localhost:5000"
echo "📧 Test the email form and modal functionality!"
echo "📝 Remember to add your Calendly URL in app.py"
echo ""
echo "Press Ctrl+C to stop the server"
echo "----------------------------------------"

python app.py 