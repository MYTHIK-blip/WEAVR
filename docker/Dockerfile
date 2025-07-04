# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY ./app/agents/weavr_agent/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all agent logic into image
COPY ./app /app

# Make sure Python sees it as a package
RUN touch /app/agents/__init__.py

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV WEAVR_ENV=production
ENV PYTHONPATH=/app

# Run the core agent
CMD ["python3", "-m", "app.agents.weavr_agent.weavr_core"]

