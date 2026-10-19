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

Test artifacts (traces, videos, screenshots) are saved to `reports/` directory.

### Docker Setup

```bash
# Build and run tests
docker-compose up --build

# Run tests and keep reports
docker-compose up

# Clean up
docker-compose down
```

## Test Artifacts

Playwright automatically generates test artifacts in `./reports/` directory:
- **Traces** - Interactive timeline of test execution
- **Videos** - Screen recordings of tests
- **Screenshots** - Images captured during tests

### View Traces

**Local:**
```bash
# View trace file interactively
npx playwright show-trace reports/trace.zip
```

**GitHub Actions:**
- Download artifacts from workflow run
- Use Playwright trace viewer to analyze failures

## Configuration

Edit `config.py` to change:
- Base URLs
- Timeouts
- Viewport size
- Expected test data

## GitHub Actions

Tests run automatically on push/PR to main branch.

**Artifacts:**
- Test traces, videos, and screenshots are uploaded as workflow artifacts
- Download from the Actions tab to analyze test results
- Use `npx playwright show-trace trace.zip` to view interactive traces

## Requirements

- Python 3.10+
- uv (package manager)
- Docker (optional)
