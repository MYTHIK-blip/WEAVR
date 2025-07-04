# civicstack/Dockerfile

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements for civicstack
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Environment
ENV PYTHONUNBUFFERED=1

# Run the dashboard script (you can swap this with FastAPI or Flask if needed)
CMD ["python", "main.py"]
