FROM python:3.10-slim

WORKDIR /app

COPY app/agents/weavr_agent/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/agents/weavr_agent/ .

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5151"]
