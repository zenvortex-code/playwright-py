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

# View test results (raw JSON files generated in allure-results/)
```

**Note:** Test results are automatically saved to `allure-results/` directory as JSON files. To view them as HTML reports, see options below.

### Docker Setup

```bash
# Build and run tests
docker-compose up --build

# Run tests and keep reports
docker-compose up

# Clean up
docker-compose down
```

Reports will be saved to:
- `./reports/` - Playwright screenshots/videos
- `./allure-results/` - Allure test results

### View Allure Reports

Allure test results are stored as JSON in `allure-results/`. To view them as HTML:

**Option 1: GitHub Pages (Easiest - No installation needed)**

View reports online after CI runs at: `https://<username>.github.io/<repo-name>/`

**Option 2: Docker (No local install needed)**
```bash
# Generate and serve HTML report
docker-compose run playwright-tests sh -c "uv run pytest && allure generate allure-results -o allure-report && allure open allure-report"
```

**Option 3: Local with Allure CLI**

Install Allure CLI:
- macOS: `brew install allure`
- Windows: `scoop install allure`
- Linux: Download from [Allure releases](https://github.com/allure-framework/allure2/releases)

Then generate HTML:
```bash
# Interactive server (recommended)
allure serve allure-results

# Or generate static HTML
allure generate allure-results -o allure-report --clean
# Open allure-report/index.html in browser
```

## Configuration

Edit `config.py` to change:
- Base URLs
- Timeouts
- Viewport size
- Expected test data

## GitHub Actions

Tests run automatically on push/PR to main branch. Allure reports are published to GitHub Pages.

**Setup:**
1. Enable GitHub Pages in repository settings
2. Set source to "GitHub Actions"
3. Push code to trigger workflow
4. View reports at: `https://<username>.github.io/<repo-name>/`

## Requirements

- Python 3.10+
- uv (package manager)
- Docker (optional, but recommended for Allure reports)