# Use Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy correct requirements file from full project path
COPY ../../app/agents/weavr_agent/requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Start the server (update this if you use FastAPI or Dash later)
CMD ["python", "main.py"]
