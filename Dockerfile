# Use Python 3.12 slim image for smaller size
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src
ENV FASTHTML_ENV=production
ENV PORT=8000

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast dependency management
RUN pip install uv

# Copy dependency configuration first for better Docker layer caching
COPY pyproject.toml uv.lock README.md ./

# Install dependencies using uv sync (which respects the lock file)
RUN uv sync --frozen --no-dev --no-install-project

# Copy application source code
COPY src/ ./src/
COPY tests/ ./tests/

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app

# Switch to non-root user
USER app

# Expose port
EXPOSE $PORT

# Run application with uvicorn using the virtual environment
CMD .venv/bin/uvicorn src.main_app.app:app --host 0.0.0.0 --port $PORT --timeout-keep-alive 30
