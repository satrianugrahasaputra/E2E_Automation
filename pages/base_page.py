from playwright.sync_api import Page, Locator, expect
from utils.logger import logger

class BasePage:
    """Base Page Object class that wraps Playwright operations with auto-logging."""

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        """Navigates to the specified URL."""
        logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)

    def click(self, selector: str) -> None:
        """Clicks on the element matching the selector after waiting for it."""
        logger.info(f"Clicking element: {selector}")
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str) -> None:
        """Fills the element matching the selector with the specified text."""
        logger.info(f"Filling element {selector} with value: {'******' if 'password' in selector.lower() else text}")
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        """Gets the inner text of the element matching the selector."""
        text = self.page.locator(selector).inner_text()
        logger.debug(f"Retrieved text from element {selector}: {text}")
        return text

    def is_visible(self, selector: str, timeout: float = 5000) -> bool:
        """Checks if the element matching the selector is visible within timeout."""
        try:
            self.page.locator(selector).wait_for(state="visible", timeout=timeout)
            logger.debug(f"Element {selector} is visible")
            return True
        except Exception:
            logger.debug(f"Element {selector} is not visible after {timeout}ms")
            return False

    def select_option(self, selector: str, value: str) -> None:
        """Selects an option from a dropdown matching the selector."""
        logger.info(f"Selecting option {value} from dropdown: {selector}")
        self.page.locator(selector).select_option(value=value)

    def check(self, selector: str) -> None:
        """Checks a checkbox or radio button."""
        logger.info(f"Checking element: {selector}")
        self.page.locator(selector).check()

    def uncheck(self, selector: str) -> None:
        """Unchecks a checkbox."""
        logger.info(f"Unchecking element: {selector}")
        self.page.locator(selector).uncheck()

    def upload_file(self, selector: str, file_path: str) -> None:
        """Uploads a file to an input field."""
        logger.info(f"Uploading file {file_path} to input: {selector}")
        self.page.locator(selector).set_input_files(file_path)

    def verify_url(self, expected_url: str) -> None:
        """Asserts that the current page URL matches the expected URL."""
        logger.info(f"Verifying current URL matches: {expected_url}")
        expect(self.page).to_have_url(expected_url)

    def verify_element_text(self, selector: str, expected_text: str) -> None:
        """Asserts that the element text matches the expected text."""
        logger.info(f"Verifying text of {selector} equals: {expected_text}")
        expect(self.page.locator(selector)).to_have_text(expected_text)
