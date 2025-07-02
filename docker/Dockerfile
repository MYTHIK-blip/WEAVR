# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install core dependencies
COPY agents/weavr_agent/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire WEAVR agent
COPY agents/weavr_agent/ ./weavr_agent/

# Set environment
ENV PYTHONUNBUFFERED=1

# Run agent
CMD ["bash", "weavr_agent/weavr_agent.sh"]
