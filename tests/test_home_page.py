import pytest
from pages.home_page import HomePage
from config import EXPECTED_TITLE_SUBSTRING, BASE_URL


class TestHomePage:
    """Test suite for Playwright home page."""

    def test_home_page_title(self, home_page: HomePage):
        """Verify home page title contains expected text."""
        title = home_page.get_title()
        assert EXPECTED_TITLE_SUBSTRING in title, \
            f"Expected '{EXPECTED_TITLE_SUBSTRING}' in title, but got '{title}'"

    def test_home_page_url(self, home_page: HomePage):
        """Verify home page URL is correct."""
        assert home_page.get_url() == BASE_URL + "/", \
            f"Expected URL to be '{BASE_URL}/', but got '{home_page.get_url()}'"

    def test_navbar_visible(self, home_page: HomePage):
        """Verify navigation bar is visible."""
        assert home_page.navbar.is_visible(), \
            "Navigation bar should be visible"

    def test_search_button_visible(self, home_page: HomePage):
        """Verify search button is visible."""
        assert home_page.search_button.is_visible(), \
            "Search button should be visible"

    def test_hero_title_visible(self, home_page: HomePage):
        """Verify hero title is visible and contains text."""
        assert home_page.hero_title.is_visible(), \
            "Hero title should be visible"
        hero_text = home_page.get_text(home_page.hero_title)
        assert hero_text, "Hero title should contain text"

    def test_get_started_button_visible(self, home_page: HomePage):
        """Verify Get Started button is visible."""
        assert home_page.get_started_button.is_visible(), \
            "Get Started button should be visible"

    def test_get_started_button_navigation(self, home_page: HomePage):
        """Verify clicking Get Started navigates to docs."""
        # Ensure we're on home page before clicking
        home_page.navigate(BASE_URL)

        home_page.click_get_started()
        assert "docs/intro" in home_page.get_url(), \
            f"Expected URL to contain 'docs/intro', but got '{home_page.get_url()}'"

        # Navigate back to home page for next tests
        home_page.navigate(BASE_URL)
