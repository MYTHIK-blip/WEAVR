# Base image: lightweight Python
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy Python dependencies
COPY ./agents/weavr_agent/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire WEAVR agent source code
COPY agents/weavr_agent/ ./weavr_agent/

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV WEAVR_ENV=production

# Ensure entrypoint script is executable
RUN chmod +x ./weavr_agent/weavr_agent.sh

# Set the default command to execute the WEAVR agent
CMD ["bash", "./weavr_agent/weavr_agent.sh"]
