from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config import DOCS_URL


class DocsPage(BasePage):
    """Page object for Playwright documentation page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.navigate(DOCS_URL)

    @property
    def installation_link(self) -> Locator:
        return self.sidebar.get_by_role("link", name="Installation").first

    @property
    def writing_tests_link(self) -> Locator:
        return self.sidebar.get_by_role("link", name="Writing tests", exact=True)

    @property
    def sidebar(self) -> Locator:
        return self.page.locator("aside.theme-doc-sidebar-container")

    @property
    def main_content(self) -> Locator:
        return self.page.locator("article")

    @property
    def page_title(self) -> Locator:
        return self.page.locator("article h1")

    def click_installation(self) -> None:
        """Click the Installation link."""
        self.logger.info("Clicking Installation link")
        self.click_and_wait(self.installation_link)

    def click_writing_tests(self) -> None:
        """Click the Writing tests link."""
        self.logger.info("Clicking Writing tests link")
        self.click_and_wait(self.writing_tests_link)
