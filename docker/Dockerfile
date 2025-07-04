FROM python:3.10-slim

WORKDIR /app

# Copy requirements file
COPY app/agents/weavr_agent/requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all weavr_agent code
COPY app/agents/weavr_agent/ .

# Runtime environment
ENV PYTHONUNBUFFERED=1

# Run the agent
CMD ["python", "main.py"]
