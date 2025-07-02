# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY ./agents/weavr_agent/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent logic
COPY ./agents /app/agents

# Environment vars
ENV PYTHONUNBUFFERED=1
ENV WEAVR_ENV=production

# Ensure shell script is executable
RUN chmod +x ./agents/weavr_agent/weavr_agent.sh

# Run script (prevent exit with tail)
CMD ["/bin/bash", "-c", "./agents/weavr_agent/weavr_agent.sh && tail -f /dev/null"]
