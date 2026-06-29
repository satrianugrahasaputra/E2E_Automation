from pages.base_page import BasePage
from locators.register_locators import RegisterLocators
from utils.logger import logger

class RegisterPage(BasePage):
    """Page Object for the Register Page."""

    def navigate_to_register(self, base_url: str) -> None:
        """Navigates to the register page."""
        url = f"{base_url}/register.html"
        self.navigate(url)

    def input_username(self, username: str) -> None:
        """Inputs the username."""
        self.fill(RegisterLocators.USERNAME_INPUT, username)

    def input_email(self, email: str) -> None:
        """Inputs the email address."""
        self.fill(RegisterLocators.EMAIL_INPUT, email)

    def input_password(self, password: str) -> None:
        """Inputs the password."""
        self.fill(RegisterLocators.PASSWORD_INPUT, password)

    def input_confirm_password(self, password: str) -> None:
        """Inputs the confirm password field."""
        self.fill(RegisterLocators.CONFIRM_PASSWORD_INPUT, password)

    def click_register(self) -> None:
        """Clicks the register submit button."""
        self.click(RegisterLocators.REGISTER_BUTTON)

    def verify_register_success(self) -> None:
        """Verifies that the registration success toast/message is displayed."""
        logger.info("Verifying registration success message")
        self.verify_element_text(RegisterLocators.SUCCESS_MESSAGE, "Registration successful! Redirecting...")

    def verify_register_failed(self, expected_error: str) -> None:
        """Verifies registration error message."""
        logger.info(f"Verifying registration error message: '{expected_error}'")
        self.verify_element_text(RegisterLocators.ERROR_MESSAGE, expected_error)
