# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY ./agents/weavr_agent/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all agent logic into image
COPY ./agents /app/agents

# Make sure Python sees it as a package
RUN touch /app/agents/__init__.py

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV WEAVR_ENV=production
ENV PYTHONPATH=/app

# Run the core agent
CMD ["python", "/app/agents/weavr_agent/weavr_core.py"]
