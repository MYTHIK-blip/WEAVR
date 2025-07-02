# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY ./agents/weavr_agent/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent directory with full path context
COPY ./agents /app/agents

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV WEAVR_ENV=production

# Ensure script is executable
RUN chmod +x ./agents/weavr_agent/weavr_agent.sh

# Run boot script
CMD ["bash", "./agents/weavr_agent/weavr_agent.sh"]
