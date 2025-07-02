#!/bin/bash
# WEAVR Agent: Boot Script

echo "🧠 WEAVR agent initializing..."
echo "🔍 Preparing discovery and stackweaving pipeline..."

# Load env variables
if [ -f .env ]; then
    export $(cat .env | xargs)
    echo "📦 Environment variables loaded."
fi

# Start pipeline logic
python3 agents/weavr_agent/glue_agent.py
