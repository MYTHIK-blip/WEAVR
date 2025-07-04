FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements for civicstack
COPY app/agents/weavr_agent/requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY app/agents/weavr_agent/ .

# Environment
ENV PYTHONUNBUFFERED=1

# Run the dashboard script (Dash, Flask, or FastAPI)
CMD ["python", "main.py"]
