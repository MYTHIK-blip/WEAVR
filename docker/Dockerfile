FROM python:3.10-slim

WORKDIR /app

# Copy requirements for weavr_agent
COPY app/agents/weavr_agent/requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all agent files
COPY app/agents/weavr_agent/ ./

# Environment
ENV PYTHONUNBUFFERED=1

# Run the agent
CMD ["python", "main.py"]
