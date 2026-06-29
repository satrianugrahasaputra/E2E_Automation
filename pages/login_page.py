from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.logger import logger

class LoginPage(BasePage):
    """Page Object for the Login Page."""

    def navigate_to_login(self, base_url: str) -> None:
        """Navigates to the login page."""
        url = f"{base_url}/login.html"
        self.navigate(url)

    def input_username(self, username: str) -> None:
        """Inputs the username into the username field."""
        self.fill(LoginLocators.USERNAME_INPUT, username)

    def input_password(self, password: str) -> None:
        """Inputs the password into the password field."""
        self.fill(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self) -> None:
        """Clicks the login button."""
        self.click(LoginLocators.LOGIN_BUTTON)

    def verify_login_success(self) -> None:
        """Asserts that login was successful by checking the success message."""
        logger.info("Verifying login success message")
        self.verify_element_text(LoginLocators.SUCCESS_MESSAGE, "Login successful!")

    def verify_login_failed(self, expected_error: str) -> None:
        """Asserts that login failed with the correct error message."""
        logger.info(f"Verifying login error message: '{expected_error}'")
        self.verify_element_text(LoginLocators.ERROR_MESSAGE, expected_error)
