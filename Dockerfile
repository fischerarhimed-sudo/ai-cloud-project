FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app .

# Railway provides PORT env variable
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
