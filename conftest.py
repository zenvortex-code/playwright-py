import pytest
import logging
import os
from playwright.sync_api import Page, Browser
from pages.home_page import HomePage
from pages.docs_page import DocsPage
from config import DEFAULT_VIEWPORT

# Ensure reports directory exists before logging is configured
os.makedirs('reports', exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('reports/test.log'),
        logging.StreamHandler()
    ]
)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": DEFAULT_VIEWPORT,
    }


@pytest.fixture(scope="class")
def page(browser: Browser):
    """Create a page instance per test class for better isolation."""
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture(scope="class")
def home_page(page: Page):
    """Create HomePage instance per test class."""
    return HomePage(page)


@pytest.fixture(scope="class")
def docs_page(page: Page):
    """Create DocsPage instance per test class."""
    return DocsPage(page)
