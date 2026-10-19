from playwright.sync_api import Page, Locator
from pages.base_page import BasePage
from config import BASE_URL


class HomePage(BasePage):
    """Page object for Playwright home page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.navigate(BASE_URL)

    @property
    def get_started_button(self) -> Locator:
        return self.page.get_by_role("link", name="Get started")

    @property
    def search_button(self) -> Locator:
        return self.page.get_by_role("button", name="Search")

    @property
    def docs_link(self) -> Locator:
        return self.page.get_by_role("link", name="Docs")

    @property
    def api_link(self) -> Locator:
        return self.page.get_by_role("link", name="API")

    @property
    def hero_title(self) -> Locator:
        return self.page.locator("h1.hero__title")

    @property
    def navbar(self) -> Locator:
        return self.page.locator("nav.navbar")

    def click_get_started(self) -> None:
        """Click the Get Started button."""
        self.logger.info("Clicking Get Started button")
        self.click_and_wait(self.get_started_button)

    def click_docs(self) -> None:
        """Click the Docs link."""
        self.logger.info("Clicking Docs link")
        self.click_and_wait(self.docs_link)

    def click_api(self) -> None:
        """Click the API link."""
        self.logger.info("Clicking API link")
        self.click_and_wait(self.api_link)
