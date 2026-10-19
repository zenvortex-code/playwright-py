FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY pytest.ini ./
COPY config.py ./
COPY conftest.py ./
COPY pages/ ./pages/
COPY tests/ ./tests/

# Install dependencies
RUN uv sync --no-cache

# Install Playwright browsers
RUN uv run playwright install --with-deps chromium

# Create reports directory
RUN mkdir -p reports/screenshots

# Run tests by default
CMD ["uv", "run", "pytest", "-v"]
