# Test Reports Directory

This directory contains test execution reports and artifacts.

## Generated Files

After running tests with `uv run pytest`, you'll find:

- **`index.html`** - Main HTML test report with test results
- **`test.log`** - Test execution logs

**Note:** Playwright artifacts (traces, videos, screenshots) are stored in the `test-results/` directory.

## Viewing Reports

**HTML Report:**
```bash
# macOS
open reports/index.html

# Windows
start reports/index.html

# Linux
xdg-open reports/index.html
```

**Trace Files:**
```bash
npx playwright show-trace test-results/trace.zip
```

## CI/CD

In GitHub Actions, reports are:
- Published to GitHub Pages
- Available as workflow artifacts

**Note:** All files in this directory except `.gitkeep` and `README.md` are git-ignored.
