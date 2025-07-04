FROM python:3.10-slim

WORKDIR /app

# Copy full app into container
COPY app/ app/

# Install requirements (update path if using shared requirements file)
RUN pip install --no-cache-dir -r app/agents/weavr_agent/requirements.txt

# Run with explicit module path
CMD ["uvicorn", "app.agents.weavr_agent.main:app", "--host", "0.0.0.0", "--port", "5151"]
