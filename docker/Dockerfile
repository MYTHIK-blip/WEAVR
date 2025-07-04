FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements for weavr_agent
COPY ../app/agents/weavr_agent/requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all weavr_agent files into the container
COPY ../app/agents/weavr_agent/ .

# Environment
ENV PYTHONUNBUFFERED=1

# Run the dashboard or agent script
CMD ["python", "main.py"]
