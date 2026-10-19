# playwright-py

Playwright + pytest test framework for https://playwright.dev/ 


## Project Structure

```
playwright-py/
├── pages/              # Page Object Model classes
│   ├── base_page.py   # Base class with common methods
│   ├── home_page.py   # Home page object
│   └── docs_page.py   # Docs page object
├── tests/              # Test suites
│   ├── test_home_page.py
│   └── test_docs_page.py
├── config.py           # Configuration constants
├── conftest.py         # pytest fixtures
├── pytest.ini          # pytest configuration
└── reports/            # Test results (git-ignored)
```

## Setup & Run

### Local Setup

```bash
# Install dependencies
uv sync

# Install Playwright browsers
uv run playwright install

# Run tests
uv run pytest

# Run with headed mode
uv run pytest --headed

# Run specific test file
uv run pytest tests/test_home_page.py -v
```

### Docker Setup

```bash
# Build and run tests
docker-compose up --build

# Run tests and keep reports
docker-compose up

# Clean up
docker-compose down
```

Reports will be saved to `./reports/` directory.

## Configuration

Edit `config.py` to change:
- Base URLs
- Timeouts
- Viewport size
- Expected test data

## Requirements

- Python 3.10+
- uv (package manager)
- Docker (optional)