import pytest
from pages.docs_page import DocsPage
from config import EXPECTED_TITLE_SUBSTRING, DOCS_URL


class TestDocsPage:
    """Test suite for Playwright documentation page."""

    def test_docs_page_title(self, docs_page: DocsPage):
        """Verify docs page title contains expected text."""
        title = docs_page.get_title()
        assert EXPECTED_TITLE_SUBSTRING in title, \
            f"Expected '{EXPECTED_TITLE_SUBSTRING}' in title, but got '{title}'"

    def test_docs_page_url(self, docs_page: DocsPage):
        """Verify docs page URL is correct."""
        assert docs_page.get_url() == DOCS_URL, \
            f"Expected URL to be '{DOCS_URL}', but got '{docs_page.get_url()}'"

    def test_sidebar_visible(self, docs_page: DocsPage):
        """Verify sidebar is visible."""
        assert docs_page.sidebar.is_visible(), \
            "Sidebar should be visible"

    def test_main_content_visible(self, docs_page: DocsPage):
        """Verify main content area is visible."""
        assert docs_page.main_content.is_visible(), \
            "Main content should be visible"

    def test_page_title_visible(self, docs_page: DocsPage):
        """Verify page title is visible."""
        assert docs_page.page_title.is_visible(), \
            "Page title should be visible"

    def test_installation_link_visible(self, docs_page: DocsPage):
        """Verify Installation link is present."""
        assert docs_page.installation_link.is_visible(), \
            "Installation link should be visible"

    def test_writing_tests_link_visible(self, docs_page: DocsPage):
        """Verify Writing tests link is present."""
        assert docs_page.writing_tests_link.is_visible(), \
            "Writing tests link should be visible"
