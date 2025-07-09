import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError
import pytest

load_dotenv()
BASE_URL = os.getenv("BASE_URL_WEB")


# This pytest hook allows you to add custom command-line options (flags)
# so users can pass additional arguments when running pytest, such as --width and --height
def pytest_addoption(parser):
    parser.addoption(
        "--width",
        action="store",
        default="1536",
        help="Browser viewport width"
    )
    parser.addoption(
        "--height",
        action="store",
        default="800",
        help="Browser viewport height"
    )


# This fixture retrieves the width and height options from the command line
# and returns them as a dictionary, converting both values to integers
@pytest.fixture
def viewport_size(request):
    return {
        "width": int(request.config.getoption("--width")),  # Get the --width value
        "height": int(request.config.getoption("--height"))  # Get the --height value
    }


# This fixture sets up the page with the specified viewport size,
@pytest.fixture(scope="function")
def set_up_tear_down(page: Page, viewport_size) -> Page:
    try:
        page.set_viewport_size(viewport_size)
        page.goto(BASE_URL, timeout=10000)
        expect(page).to_have_url(BASE_URL, timeout=3000)
        yield page
    except PlaywrightTimeoutError:
        pytest.fail("Page load or element lookup timed out – check your internet connection or server status.")
    except Exception as e:
        pytest.fail(f"Unexpected error during setup: {e}")
