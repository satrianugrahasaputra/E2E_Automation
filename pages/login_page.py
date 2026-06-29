from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.logger import logger

class LoginPage(BasePage):
    """Page Object for the Login Page supporting both SauceDemo and local mock app."""

    def navigate_to_login(self, base_url: str) -> None:
        """Navigates to the login page."""
        if "saucedemo.com" in base_url:
            url = base_url
        else:
            url = f"{base_url}/login.html"
        self.navigate(url)

    def _is_sauce(self) -> bool:
        return "saucedemo.com" in self.page.url

    def input_username(self, username: str) -> None:
        """Inputs the username."""
        selector = LoginLocators.SAUCE_USERNAME_INPUT if self._is_sauce() else LoginLocators.USERNAME_INPUT
        self.fill(selector, username)

    def input_password(self, password: str) -> None:
        """Inputs the password."""
        selector = LoginLocators.SAUCE_PASSWORD_INPUT if self._is_sauce() else LoginLocators.PASSWORD_INPUT
        self.fill(selector, password)

    def click_login(self) -> None:
        """Clicks the login button."""
        selector = LoginLocators.SAUCE_LOGIN_BUTTON if self._is_sauce() else LoginLocators.LOGIN_BUTTON
        self.click(selector)

    def verify_login_success(self) -> None:
        """Asserts that login was successful."""
        logger.info("Verifying login success")
        if self._is_sauce():
            # SauceDemo redirects to the inventory page
            self.verify_url("https://www.saucedemo.com/inventory.html")
        else:
            self.verify_element_text(LoginLocators.SUCCESS_MESSAGE, "Login successful!")

    def verify_login_failed(self, expected_error: str) -> None:
        """Asserts that login failed with correct error."""
        logger.info(f"Verifying login error message: '{expected_error}'")
        if self._is_sauce():
            # In SauceDemo, standard error message for wrong password is:
            # "Epic sadface: Username and password do not match any user in this service"
            # Let's verify that the error element contains the expected error message or standard sauce error
            if "incorrect" in expected_error or "match" in expected_error:
                expected_error = "Epic sadface: Username and password do not match any user in this service"
            elif "required" in expected_error:
                if "Username" in expected_error:
                    expected_error = "Epic sadface: Username is required"
                else:
                    expected_error = "Epic sadface: Password is required"
            self.verify_element_text(LoginLocators.SAUCE_ERROR_MESSAGE, expected_error)
        else:
            self.verify_element_text(LoginLocators.ERROR_MESSAGE, expected_error)
