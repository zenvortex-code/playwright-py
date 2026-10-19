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

# View HTML report (generated after test run)
open reports/report.html  # macOS
start reports/report.html # Windows
xdg-open reports/report.html # Linux
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

## Test Reports

Reports are automatically saved to `./reports/` directory:
- `report.html` - Main HTML test report (self-contained)
- Screenshots and videos (on test failure)
- Trace files (on test failure)

### View Reports

**Local:**
Open `reports/report.html` in your browser after running tests.

**GitHub Pages:**
Reports are automatically published at: `https://<username>.github.io/<repo-name>/report.html`

## Configuration

Edit `config.py` to change:
- Base URLs
- Timeouts
- Viewport size
- Expected test data

## GitHub Actions

Tests run automatically on push/PR to main branch. HTML reports are published to GitHub Pages.

**Setup:**
1. Enable GitHub Pages in repository settings
2. Set source to "GitHub Actions"
3. Push code to trigger workflow
4. View reports at: `https://<username>.github.io/<repo-name>/report.html`

## Requirements

- Python 3.10+
- uv (package manager)
- Docker (optional)
