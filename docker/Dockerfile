FROM python:3.10-slim

WORKDIR /app

# Copy requirements
COPY app/agents/weavr_agent/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY app/agents/weavr_agent/ .

# Set runtime environment
ENV PYTHONUNBUFFERED=1

# Start with uvicorn (FastAPI)
CMD ["uvicorn", "weavr_agent.main:app", "--host", "0.0.0.0", "--port", "5151"]
