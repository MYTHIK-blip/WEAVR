# ─────────────────────────────────────────────
# Base image: slim Python for lightweight container
FROM python:3.10-slim

# ─────────────────────────────────────────────
# Set working directory inside container
WORKDIR /app

# ─────────────────────────────────────────────
# Copy and install Python dependencies
COPY agents/weavr_agent/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ─────────────────────────────────────────────
# Copy the entire WEAVR agent source code
COPY agents/weavr_agent/ ./weavr_agent/

# ─────────────────────────────────────────────
# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    WEAVR_ENV=production

# ─────────────────────────────────────────────
# Set the default command to execute the agent
CMD ["bash", "/app/weavr_agent/weavr_agent.sh"]
CMD ["python", "-m", "weavr_agent.main"]
