FROM python:3.10-slim

WORKDIR /app

# Copy source code
COPY app/ app/

# Install dependencies (adjust path if needed)
RUN pip install --no-cache-dir -r app/agents/weavr_agent/requirements.txt

# Expose public FastAPI port
EXPOSE 5151

# Launch Uvicorn with full module path
CMD ["uvicorn", "app.agents.weavr_agent.weavr_core:app", "--host", "0.0.0.0", "--port", "5151"]
