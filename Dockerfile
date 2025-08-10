# Use Python 3.12 slim image for smaller size
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

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
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/healthz || exit 1

# Run application with uvicorn using the virtual environment
CMD [".venv/bin/uvicorn", "src.main_app.app:app", "--host", "0.0.0.0", "--port", "8000", "--timeout-keep-alive", "30"]