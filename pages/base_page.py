from playwright.sync_api import Page, Locator
import logging
from typing import Optional
from config import DEFAULT_TIMEOUT, NAVIGATION_TIMEOUT


class BasePage:
    """Base page object with common methods for all pages."""

    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(self.__class__.__name__)

    def navigate(self, url: str, timeout: int = NAVIGATION_TIMEOUT) -> None:
        """Navigate to the specified URL."""
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url, timeout=timeout)

    def get_title(self) -> str:
        """Get the page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Get the current page URL."""
        return self.page.url

    def wait_for_load_state(self, state: str = "load") -> None:
        """Wait for page to reach specified load state."""
        self.logger.info(f"Waiting for load state: {state}")
        self.page.wait_for_load_state(state)

    def wait_for_url(self, url: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        """Wait for URL to match the specified pattern."""
        self.logger.info(f"Waiting for URL to match: {url}")
        self.page.wait_for_url(url, timeout=timeout)

    def click_and_wait(self, locator: Locator, wait_for_navigation: bool = True) -> None:
        """Click an element and optionally wait for navigation."""
        self.logger.info(f"Clicking element")
        if wait_for_navigation:
            with self.page.expect_navigation():
                locator.click()
        else:
            locator.click()

    def fill_field(self, locator: Locator, text: str) -> None:
        """Fill a text field."""
        self.logger.info(f"Filling field with: {text}")
        locator.fill(text)

    def is_visible(self, locator: Locator, timeout: int = DEFAULT_TIMEOUT) -> bool:
        """Check if element is visible."""
        try:
            return locator.is_visible(timeout=timeout)
        except Exception:
            return False

    def wait_for_element(self, locator: Locator, state: str = "visible", timeout: int = DEFAULT_TIMEOUT) -> None:
        """Wait for element to reach specified state."""
        self.logger.info(f"Waiting for element to be {state}")
        locator.wait_for(state=state, timeout=timeout)

    def get_text(self, locator: Locator) -> Optional[str]:
        """Get text content of an element."""
        return locator.text_content()

    def screenshot(self, name: str) -> None:
        """Take a screenshot."""
        path = f"reports/screenshots/{name}.png"
        self.logger.info(f"Taking screenshot: {path}")
        self.page.screenshot(path=path)
