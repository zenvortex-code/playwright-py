FROM python:3.12-slim

# Install system dependencies and Allure
RUN apt-get update && apt-get install -y \
    curl \
    default-jre \
    && curl -o allure-2.24.0.tgz -L https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz \
    && tar -zxvf allure-2.24.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure \
    && rm allure-2.24.0.tgz \
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
RUN mkdir -p reports/screenshots allure-results allure-report

# Run tests by default
CMD ["uv", "run", "pytest", "-v"]
