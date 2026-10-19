"""Configuration constants for the test framework."""

# Base URLs
BASE_URL = "https://playwright.dev"
DOCS_URL = f"{BASE_URL}/docs/intro"

# Viewport
DEFAULT_VIEWPORT = {"width": 1920, "height": 1080}

# Timeouts (in milliseconds)
DEFAULT_TIMEOUT = 30000
NAVIGATION_TIMEOUT = 30000

# Test data
EXPECTED_TITLE_SUBSTRING = "Playwright"
