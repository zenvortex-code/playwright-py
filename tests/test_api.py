import json
import pytest
from playwright.sync_api import Page, Request, Response, Route, expect

BASE_URL = "https://demo.playwright.dev"
APP_PATH = "/api-mocking"
FULL_URL = f"{BASE_URL}{APP_PATH}"
API_GLOB = "**/api/v1/fruits"



@pytest.fixture(scope="session")
def base_url() -> str:
    """Default base URL; overridden by --base-url on the command line."""
    return BASE_URL


def _is_fruits_get(response: Response) -> bool:
    """Check if response is a GET request to the fruits API."""
    request: Request = response.request
    return request.method == "GET" and "/api/v1/fruits" in response.url


class FruitsPage:
    """Page object for the fruits API mocking demo page."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.items = page.locator("ul > li")
        self.alert = page.get_by_role("alert")

    def open(self) -> None:
        """Navigate without waiting on the API (used when the API is mocked)."""
        self.page.goto(FULL_URL)

    def open_and_wait_for_api(self) -> Response:
        """Navigate and block until the initial GET /api/v1/fruits completes."""
        with self.page.expect_response(_is_fruits_get) as response_info:
            self.page.goto(FULL_URL)
        response = response_info.value
        return response


def test_list_matches_initial_api_response(page: Page) -> None:
    """UI + network sync: the rendered list mirrors the API payload."""
    fruits = FruitsPage(page)

    response = fruits.open_and_wait_for_api()
    assert response.ok, f"Initial fruits request failed: {response.status}"
    names = [item["name"] for item in response.json()]
    assert names, "API returned no fruits"

    expect(fruits.items).to_have_count(len(names))
    expect(fruits.items).to_have_text(names)


def test_mocked_response_replaces_list_data(page: Page) -> None:
    """Mock a successful response and verify only the mocked data is shown."""
    mocked = [{"name": "Strawberry", "id": 21}]
    page.route(API_GLOB, lambda route: route.fulfill(json=mocked))

    fruits = FruitsPage(page)
    fruits.open()

    expect(fruits.items).to_have_count(1)
    expect(fruits.items).to_have_text(["Strawberry"])



def test_api_failure_renders_no_list(page: Page) -> None:
    """HTTP 500 from the API: no fruit list is rendered."""

    def fail_request(route: Route) -> None:
        if route.request.method != "GET":
            route.fallback()
            return
        route.fulfill(
            status=500,
            content_type="application/json",
            body=json.dumps({"error": "Database unavailable"}),
        )

    page.route(API_GLOB, fail_request)

    fruits = FruitsPage(page)
    fruits.open()

    expect(fruits.items).to_have_count(0)

