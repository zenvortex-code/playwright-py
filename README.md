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

# Run tests (generates HTML report automatically)
uv run pytest

# Run with headed mode
uv run pytest --headed

# Run specific test file
uv run pytest tests/test_home_page.py -v

# View HTML report (generated after any test run)
open reports/index.html  # macOS
start reports/index.html # Windows
xdg-open reports/index.html # Linux
```

HTML reports are automatically generated at `reports/index.html` on every test run.

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

### HTML Reports

HTML reports are automatically generated at `reports/index.html` on every test run (both local and CI).

**Local:**
Simply run `uv run pytest` and open `reports/index.html` in your browser.

**GitHub Pages:**
View reports online at: `https://<username>.github.io/<repo-name>/`

### Playwright Traces

Playwright automatically generates test artifacts in `./reports/` directory:
- **Traces** - Interactive timeline of test execution
- **Videos** - Screen recordings of tests
- **Screenshots** - Images captured during tests

**View traces locally:**
```bash
npx playwright show-trace reports/trace.zip
```

**GitHub Actions:**
Download artifacts from workflow run to analyze with Playwright trace viewer

## Configuration

Edit `config.py` to change:
- Base URLs
- Timeouts
- Viewport size
- Expected test data

## GitHub Actions

Tests run automatically on push/PR to main branch.

**HTML Reports:**
- Automatically published to GitHub Pages
- View at: `https://<username>.github.io/<repo-name>/`

**Setup GitHub Pages:**
1. Go to repository Settings → Pages
2. Set source to "GitHub Actions"
3. Push code to trigger workflow

**Artifacts:**
- Test traces, videos, and screenshots are uploaded as workflow artifacts
- Download from Actions tab to analyze with `npx playwright show-trace trace.zip`

## Requirements

- Python 3.10+
- uv (package manager)
- Docker (optional)
