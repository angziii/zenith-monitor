#!/bin/bash

# Anti-Slacking AI Monitor Launch Script
# This script automates the setup and launch process for macOS users.

echo "🚀 Starting Anti-Slacking AI Monitor..."

# Get the directory where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

# 1. Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Initializing setup (this may take a minute)..."
    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt
fi

# 2. Check for the vision model
if [ ! -f "face_landmarker.task" ]; then
    echo "📥 Downloading AI vision model..."
    curl -L -O https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task
fi

# 3. Kill any existing process on port 8000
lsof -i :8000 -t | xargs kill -9 2>/dev/null

# 4. Open the dashboard in the default browser
echo "🌐 Opening dashboard..."
open index.html

# 5. Start the backend
echo "🧠 Starting AI engine..."
echo "------------------------------------------------"
echo "TIP: Keep this window open while using the tool."
echo "The system will auto-close if you close the webpage."
echo "------------------------------------------------"
./venv/bin/python3 main.py
