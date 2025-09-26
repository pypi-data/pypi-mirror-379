# Charlie Munger Investment Analysis - Docker Container
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy package files
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Install package with web dependencies
RUN pip install --no-cache-dir -e ".[web]"

# Create non-root user
RUN useradd --create-home --shell /bin/bash munger
RUN chown -R munger:munger /app
USER munger

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run web API
CMD ["munger-web", "--host", "0.0.0.0", "--port", "8000"]