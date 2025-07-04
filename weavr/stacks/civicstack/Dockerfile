FROM python:3.10-slim

WORKDIR /app

# Copy requirement files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Environment
ENV PYTHONUNBUFFERED=1

# Run your dashboard (could be Dash, Flask, or FastAPI)
CMD ["python", "main.py"]
